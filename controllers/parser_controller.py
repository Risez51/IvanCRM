import main_window
import os
from controllers import view_config as vc
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QTreeWidgetItem, QComboBox
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from controllers import worker
from actions.supplier_parser import SupplierParser


class ParserController:
    def __init__(self, ui: main_window.Ui_MainWindow):
        self.ui = ui
        self.thread = QtCore.QThread()
        self.my_worker = worker.Worker()
        self.my_worker.moveToThread(self.thread)

        self.my_worker.supplier_parser_item_started.connect(self.on_supplier_parser_item_started)
        self.my_worker.supplier_parser_item_finished.connect(self.on_supplier_parser_item_finished)
        self.my_worker.supplier_parser_finished.connect(self.on_supplier_parser_finished)
        self.thread.started.connect(self.my_worker.run_supplier_parser)

        # GUI element connectors
        self.ui.add_price_push_button.clicked.connect(self.on_add_price_push_button)
        self.ui.delete_price_push_botton.clicked.connect(self.on_delete_price_push_button)
        self.ui.start_parsing_push_button.clicked.connect(self.on_start_parsing_push_button)
        self.ui.add_result_path_parser_push_button.clicked.connect(self.on_add_result_path_parser_push_button)
        self.ui.test_parser_push_button.clicked.connect(self.combobox_to_text)

    def on_add_price_push_button(self):
        opened_files = QFileDialog.getOpenFileNames(None, 'Выберите паспорта .doc .pdf', '', '*.xls *.xlsx *.csv')

        for file in opened_files[0]:
            combobox = QComboBox()
            combobox.addItems(vc.SUPPLIERS)
            tree_item = QTreeWidgetItem(self.ui.manual_parser_tree_widget)
            tree_item.setText(0, os.path.abspath(os.path.dirname(file)))
            tree_item.setText(1, os.path.basename(file))
            self.ui.manual_parser_tree_widget.setItemWidget(tree_item, 2, combobox)

    def on_delete_price_push_button(self):
        for item in self.ui.manual_parser_tree_widget.selectedItems():
            self.ui.manual_parser_tree_widget.invisibleRootItem().removeChild(item)

    def on_add_result_path_parser_push_button(self):
        specified_dir = os.path.abspath(QFileDialog.getExistingDirectory(None, 'Выберите папку'))
        self.ui.result_path_parser_line_edit.setText(specified_dir)

    # Start parsing files
    def on_start_parsing_push_button(self):
        files_dict = self.__get_values_from_tree_widget_items()
        print(files_dict)
        output_dir = self.ui.result_path_parser_line_edit.text()
        self.my_worker.set_params(files_dict, output_dir)
        self.thread.start()

    def __get_values_from_tree_widget_items(self) -> dict:
        root = self.ui.manual_parser_tree_widget.invisibleRootItem()
        item_index_sup_file_dict = {}
        for item_index in range(root.childCount()):
            item = root.child(item_index)
            combobox = self.ui.manual_parser_tree_widget.itemWidget(item, 2)
            combobox_value = combobox.currentText()
            combobox.hide()
            item.setText(2, combobox_value)
            dir_path_value = item.text(0)
            filename_value = item.text(1)
            supplier_name = item.text(2)
            price_file_path = dir_path_value + '\\' + filename_value
            item_index_sup_file_dict[item_index] = {supplier_name: price_file_path}

        # Возвращает {treeWidgetItem_index: {supplier_name: price_file_path}}
        return item_index_sup_file_dict

    # Make text cell from combobox value
    def combobox_to_text(self):
        item = self.ui.manual_parser_tree_widget.invisibleRootItem().child(0)
        combobox = self.ui.manual_parser_tree_widget.itemWidget(item, 2)
        combobox_value = self.ui.manual_parser_tree_widget.itemWidget(item, 2).currentText()
        combobox.hide()
        item.setText(2, combobox_value)


    # THREAD SLOTS
    def on_supplier_parser_item_started(self, item_index):
        self.__set_tree_item_status(item_index, vc.STATUS_PROCESSING_COLOR)

    def on_supplier_parser_item_finished(self, item_index):
        self.__set_tree_item_status(item_index, vc.STATUS_READY_COLOR)

    def on_supplier_parser_finished(self):
        self.thread.quit()
        self.__show_message_on_result_ready()

    # Private functions
    def __set_tree_item_status(self, item_index: int, color_hex: str):
        color = QColor(color_hex)
        # Set columns color
        self.ui.manual_parser_tree_widget.invisibleRootItem().child(item_index).setBackground(0, color)
        self.ui.manual_parser_tree_widget.invisibleRootItem().child(item_index).setBackground(1, color)
        self.ui.manual_parser_tree_widget.invisibleRootItem().child(item_index).setBackground(2, color)

        # Set combobox color
        # item = self.ui.manual_parser_tree_widget.invisibleRootItem().child(item_index)
        # combobox = self.ui.manual_parser_tree_widget.itemWidget(item, 2)
        # combobox.setStyleSheet('QComboBox{background-color: ' + color_hex + ';}')

    def __show_message_on_result_ready(self):
        msg_answer = QMessageBox.question(None, 'Парсинг файлов окончен',
                                          'Открыть папку с файлами?',
                                          QMessageBox.Yes, QMessageBox.No)
        if msg_answer == QMessageBox.Yes:
            result_path = self.ui.result_path_parser_line_edit.text()
            os.system(r'explorer.exe ' + f'{result_path}')
