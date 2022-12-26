import main_window
import os
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QTreeWidgetItem, QComboBox
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from controllers import worker
from configs import config


class ParserController:
    def __init__(self, ui: main_window.Ui_MainWindow):
        self.ui = ui
        # Thread manual parser
        self.thread_manual_parser = QtCore.QThread()
        self.my_worker_manual = worker.Worker()
        self.my_worker_manual.moveToThread(self.thread_manual_parser)
        # Thread automatic parser
        self.thread_auto_parser = QtCore.QThread()
        self.my_worker_automatic = worker.Worker()
        self.my_worker_automatic.moveToThread(self.thread_auto_parser)
        # Thread manual connectors
        self.my_worker_manual.manual_suppler_parser_started.connect(self.on_manual_supplier_parser_started)
        self.my_worker_manual.manual_supplier_parser_item_started.connect(self.on_manual_supplier_parser_item_started)
        self.my_worker_manual.manual_supplier_parser_item_finished.connect(self.on_manual_supplier_parser_item_finished)
        self.my_worker_manual.manual_supplier_parser_finished.connect(self.on_manual_supplier_parser_finished)
        self.thread_manual_parser.started.connect(self.my_worker_manual.run_manual_supplier_parser)
        # Thread automatic connectors
        self.my_worker_automatic.automatic_supplier_parser_started.connect(self.on_automatic_parser_started)
        self.my_worker_automatic.automatic_supplier_parser_finished.connect(self.on_automatic_parser_finished)
        self.thread_auto_parser.started.connect(self.my_worker_automatic.run_automatic_supplier_parser)
        # GUI element connectors manual parser
        self.ui.add_price_push_button.clicked.connect(self.on_add_price_push_button)
        self.ui.delete_price_push_button.clicked.connect(self.on_delete_price_push_button)
        self.ui.start_parsing_push_button.clicked.connect(self.on_start_parsing_push_button)
        self.ui.add_result_path_parser_push_button.clicked.connect(self.on_add_result_path_parser_push_button)
        self.ui.add_multiple_price_push_button.clicked.connect(self.on_add_multiple_price_push_button)
        # GUI element auto parser initialize
        self.ui.link_kvt_line_edit.setText(config.KVT_LINK)
        self.ui.link_torg7_line_edit.setText(config.TOG7_LINK)
        self.ui.link_a4_line_edit.setText(config.A4_LINK)
        # GUI element connectors automatic parser
        self.ui.parse_kvt_push_button.clicked.connect(self.parse_kvt)
        self.ui.parse_torg7_push_button.clicked.connect(self.parse_torg7)
        self.ui.parse_a4_push_button.clicked.connect(self.parse_a4)
        # TEST
        self.ui.test_push_button.clicked.connect(self.test)

    # MANUAL PARSER ELEMENTS+++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Added files to treeWidget as treeWidgetItems
    def on_add_price_push_button(self):
        opened_files = QFileDialog.getOpenFileNames(None, 'Выберите файлы .xls, .xlsx, .xml', '',
                                                    '*.xls *.xlsx *.csv *.xml')
        if opened_files[0]:
            for file_path in opened_files[0]:
                self.__create_new_tree_widget_item(file_path)

    def on_add_multiple_price_push_button(self):
        opened_files = QFileDialog.getOpenFileNames(None, 'Выберите файлы .xls, .xlsx, .xml', '',
                                                    '*.xls *.xlsx *.csv *.xml')
        if opened_files[0]:
            self.__create_new_tree_widget_item_multiple(opened_files[0])

    def __create_new_tree_widget_item_multiple(self, files_list):
        tree_widget_item = QTreeWidgetItem(self.ui.manual_parser_tree_widget)
        tree_widget_item.setText(0, os.path.abspath(os.path.dirname(files_list[0])))
        file_names = ''
        for file_path in files_list:
            file_names += os.path.basename(file_path) + ';'
        tree_widget_item.setText(1, os.path.basename(file_names))
        self.__add_combobox_to_manual_parser_tree_widget_item(2, tree_widget_item)

    # Delete tree_widget_item
    def on_delete_price_push_button(self):
        for item in self.ui.manual_parser_tree_widget.selectedItems():
            self.ui.manual_parser_tree_widget.invisibleRootItem().removeChild(item)

    # Added result path to line edit
    def on_add_result_path_parser_push_button(self):
        specified_dir = os.path.abspath(QFileDialog.getExistingDirectory(None, 'Выберите папку'))
        self.ui.result_path_parser_line_edit.setText(specified_dir)

    # Start parsing files
    def on_start_parsing_push_button(self):
        if self.ui.manual_parser_tree_widget.invisibleRootItem().childCount() > 0 and \
                self.ui.result_path_parser_line_edit.text() != '':
            files_dict = self.__get_values_from_tree_widget_items()
            output_dir = self.ui.result_path_parser_line_edit.text()
            self.my_worker_manual.set_manual_parser_params(files_dict, output_dir)
            self.thread_manual_parser.start()
    # MANUAL PARSER ELEMENTS----------------------------------------------------

    # AUTOMATIC PARSER ELEMENTS+++++++++++++++++++++++++++++++++++++++++++++++++
    def parse_kvt(self):
        if self.ui.result_path_parser_line_edit.text() != '':
            link = self.ui.link_kvt_line_edit.text()
            output_path = self.ui.result_path_parser_line_edit.text()
            self.my_worker_automatic.set_automatic_parser_params(config.KVT_NAME, link, output_path)
            self.thread_auto_parser.start()

    def parse_torg7(self):
        if self.ui.result_path_parser_line_edit.text() != '':
            link = self.ui.link_torg7_line_edit.text()
            output_path = self.ui.result_path_parser_line_edit.text()
            self.my_worker_automatic.set_automatic_parser_params(config.TORG7_NAME, link, output_path)
            self.thread_auto_parser.start()

    def parse_a4(self):
        if self.ui.result_path_parser_line_edit.text() != '':
            link = self.ui.link_a4_line_edit.text()
            output_path = self.ui.result_path_parser_line_edit.text()
            self.my_worker_automatic.set_automatic_parser_params(config.A4_NAME, link, output_path)
            self.thread_auto_parser.start()
    # AUTOMATIC PARSER ELEMENTS------------------------------------------------

    def __create_new_tree_widget_item(self, file_path):
        tree_widget_item = QTreeWidgetItem(self.ui.manual_parser_tree_widget)
        tree_widget_item.setText(0, os.path.abspath(os.path.dirname(file_path)))
        tree_widget_item.setText(1, os.path.basename(file_path))
        self.__add_combobox_to_manual_parser_tree_widget_item(2, tree_widget_item)

    def __add_combobox_to_manual_parser_tree_widget_item(self, column: int, tree_widget_item: QTreeWidgetItem):
        combobox = QComboBox()
        combobox.addItems(config.SUPPLIERS)
        self.ui.manual_parser_tree_widget.setItemWidget(tree_widget_item, column, combobox)

    # Return values from tree_widget {treeWidgetItem_index: {supplier_name: price_file_path}}
    # Where supplier_name = combobox value, price_file_path = dir_path + filename
    def __get_values_from_tree_widget_items(self) -> dict:
        root = self.ui.manual_parser_tree_widget.invisibleRootItem()
        item_index_sup_file_dict = {}
        for item_index in range(root.childCount()):
            tree_widget_item = root.child(item_index)
            self.convert_combobox_to_text(tree_widget_item, 2)
            item_index_sup_file_dict[item_index] = self.__get_values_from_tree_widget_item(tree_widget_item)
        return item_index_sup_file_dict

    # Return values from tree_widget_item columns
    @staticmethod
    def __get_values_from_tree_widget_item(tree_widget_item: QTreeWidgetItem) -> dict:
        dir_path = tree_widget_item.text(0)
        filename = tree_widget_item.text(1)
        supplier_name = tree_widget_item.text(2)
        file_path = dir_path + '\\' + filename
        return {supplier_name: file_path}

    # Make text cell from combobox value
    def convert_combobox_to_text(self, tree_widget_item: QTreeWidgetItem, column: int):
        if isinstance(self.ui.manual_parser_tree_widget.itemWidget(tree_widget_item, column), QComboBox):
            combobox_value = self.ui.manual_parser_tree_widget.itemWidget(tree_widget_item, column).currentText()
            self.ui.manual_parser_tree_widget.removeItemWidget(tree_widget_item, column)
            tree_widget_item.setText(column, combobox_value)

    # Sets the color for tree_widget_item
    def __set_tree_widget_item_color(self, item_index: int, color_hex: str):
        color = QColor(color_hex)
        self.ui.manual_parser_tree_widget.invisibleRootItem().child(item_index).setBackground(0, color)
        self.ui.manual_parser_tree_widget.invisibleRootItem().child(item_index).setBackground(1, color)
        self.ui.manual_parser_tree_widget.invisibleRootItem().child(item_index).setBackground(2, color)

    # shows a message and offers to open the folder with the result of parsing
    def __show_message_on_result_ready(self):
        msg_answer = QMessageBox.question(None, 'Парсинг файлов окончен',
                                          'Открыть папку с файлами?',
                                          QMessageBox.Yes, QMessageBox.No)
        if msg_answer == QMessageBox.Yes:
            result_path = self.ui.result_path_parser_line_edit.text()
            os.system(r'explorer.exe ' + f'{result_path}')

    # THREAD SLOTS MANUAL PARSING
    # On started manual parsing
    def on_manual_supplier_parser_started(self):
        self.ui.start_parsing_push_button.setEnabled(False)
        self.ui.delete_price_push_button.setEnabled(False)
        self.ui.add_result_path_parser_push_button.setEnabled(False)
        self.ui.add_price_push_button.setEnabled(False)

    # On started manual parsing supplier_price changing color(status)
    def on_manual_supplier_parser_item_started(self, item_index: int):
        self.__set_tree_widget_item_color(item_index, config.STATUS_PROCESSING_COLOR)

    # On finished manual parsing supplier_price changing color(status)
    def on_manual_supplier_parser_item_finished(self, item_index: int):
        self.__set_tree_widget_item_color(item_index, config.STATUS_READY_COLOR)

    # On finished manual parsing all supplier_prices
    def on_manual_supplier_parser_finished(self):
        self.ui.add_result_path_parser_push_button.setEnabled(True)
        self.ui.delete_price_push_button.setEnabled(True)
        self.ui.start_parsing_push_button.setEnabled(True)
        self.ui.add_price_push_button.setEnabled(True)
        self.thread_manual_parser.quit()
        self.__show_message_on_result_ready()

    # THREAD SLOTS AUTOMATIC PARSER
    def on_automatic_parser_started(self, supplier_name):
        color = 'QLineEdit {background: ' + config.STATUS_PROCESSING_COLOR + ';}'
        if supplier_name == config.KVT_NAME:
            self.ui.link_kvt_line_edit.setStyleSheet(color)
            self.ui.parse_kvt_push_button.setEnabled(False)
        elif supplier_name == config.TORG7_NAME:
            self.ui.link_torg7_line_edit.setStyleSheet(color)
        elif supplier_name == config.A4_NAME:
            self.ui.link_a4_line_edit.setStyleSheet(color)

    def on_automatic_parser_finished(self, supplier_name):
        color = 'QLineEdit {background: ' + config.STATUS_READY_COLOR + ';}'
        if supplier_name == config.KVT_NAME:
            self.ui.link_kvt_line_edit.setStyleSheet(color)
            self.ui.parse_kvt_push_button.setEnabled(True)
        elif supplier_name == config.TORG7_NAME:
            self.ui.link_torg7_line_edit.setStyleSheet(color)
        elif supplier_name == config.A4_NAME:
            self.ui.link_a4_line_edit.setStyleSheet(color)
        self.thread_auto_parser.quit()

    def test(self):
        self.ui.delete_price_push_button.setEnabled(True)
