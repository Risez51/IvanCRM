from controllers.speaker import Speaker
import main_window
import os
from PyQt5.QtWidgets import QFileDialog, QTreeWidgetItem, QComboBox
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
        self.my_worker_manual.manual_supplier_parser_error.connect(self.on_manual_parsing_error)
        self.thread_manual_parser.started.connect(self.my_worker_manual.run_manual_supplier_parser)
        # Thread automatic connectors
        self.my_worker_automatic.automatic_supplier_parser_started.connect(self.on_automatic_parser_started)
        self.my_worker_automatic.automatic_supplier_parser_finished.connect(self.on_automatic_parser_finished)
        self.my_worker_automatic.automatic_supplier_parser_error.connect(self.on_automatic_parsing_error)
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
        self.ui.parse_kvt_push_button.clicked.connect(self.on_parse_kvt_push_button)
        self.ui.parse_torg7_push_button.clicked.connect(self.on_parse_torg7_push_button)
        self.ui.parse_a4_push_button.clicked.connect(self.on_parse_a4_push_button)
        # TEST
        self.ui.test_push_button.clicked.connect(self.test)

    # MANUAL PARSER ELEMENTS+++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Добавлет в TreeWidgetItem для 1 файла
    def on_add_price_push_button(self):
        opened_files: list = QFileDialog.getOpenFileNames(None, 'Выберите файлы', '',
                                                          config.PRICE_FILE_TYPES)
        if opened_files[0]:
            for file_path in opened_files[0]:
                self.__create_new_tree_widget_item(file_path)

    # Добавлет в TreeWidgetItem для нескольких файлов
    def on_add_multiple_price_push_button(self):
        opened_files: list = QFileDialog.getOpenFileNames(None, 'Выберите файлы', '',
                                                          config.PRICE_FILE_TYPES)
        if opened_files[0]:
            self.__create_new_tree_widget_item_multiple(opened_files[0])

    # Удаляет выбранный TreeWidgetItem
    def on_delete_price_push_button(self):
        for item in self.ui.manual_parser_tree_widget.selectedItems():
            self.ui.manual_parser_tree_widget.invisibleRootItem().removeChild(item)

    # Заполняет поле "Результирующий путь"
    def on_add_result_path_parser_push_button(self):
        specified_dir: str = os.path.abspath(QFileDialog.getExistingDirectory(None, 'Выберите папку'))
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
    def on_parse_a4_push_button(self):
        if self.ui.result_path_parser_line_edit.text() != '':
            link: str = self.ui.link_a4_line_edit.text()
            output_path: str = self.ui.result_path_parser_line_edit.text()
            self.my_worker_automatic.set_automatic_parser_params(config.A4_NAME, link, output_path)
            self.thread_auto_parser.start()

    def on_parse_kvt_push_button(self):
        if self.ui.result_path_parser_line_edit.text() != '':
            link: str = self.ui.link_kvt_line_edit.text()
            output_path: str = self.ui.result_path_parser_line_edit.text()
            self.my_worker_automatic.set_automatic_parser_params(config.KVT_NAME, link, output_path)
            self.thread_auto_parser.start()

    def on_parse_torg7_push_button(self):
        if self.ui.result_path_parser_line_edit.text() != '':
            link: str = self.ui.link_torg7_line_edit.text()
            output_path: str = self.ui.result_path_parser_line_edit.text()
            self.my_worker_automatic.set_automatic_parser_params(config.TORG7_NAME, link, output_path)
            self.thread_auto_parser.start()

    # AUTOMATIC PARSER ELEMENTS------------------------------------------------

    # Создает TreeWidgetItem из 1 файла
    def __create_new_tree_widget_item(self, file_path: str):
        tree_widget_item = QTreeWidgetItem(self.ui.manual_parser_tree_widget)
        tree_widget_item.setText(0, os.path.abspath(os.path.dirname(file_path)))
        tree_widget_item.setText(1, os.path.basename(file_path))
        self.__add_combobox_to_manual_parser_tree_widget_item(2, tree_widget_item)

    # Создает TreeWidgetItem из нескольких файлов
    def __create_new_tree_widget_item_multiple(self, files_list: list):
        tree_widget_item = QTreeWidgetItem(self.ui.manual_parser_tree_widget)
        tree_widget_item.setText(0, os.path.abspath(os.path.dirname(files_list[0])))
        file_names: str = ''
        # fn = [os.path.basename(file_path) for file_path in files_list]
        for file_path in files_list:
            file_names += os.path.basename(file_path) + ';'
        tree_widget_item.setText(1, file_names)
        self.__add_combobox_to_manual_parser_tree_widget_item(2, tree_widget_item)

    # Создает комбобокс со списком поставщиков в TreeWidgetItem
    def __add_combobox_to_manual_parser_tree_widget_item(self, column: int, tree_widget_item: QTreeWidgetItem):
        combobox = QComboBox()
        combobox.addItems(config.SUPPLIERS)
        self.ui.manual_parser_tree_widget.setItemWidget(tree_widget_item, column, combobox)

    # Возвращает словрь значений всех TreeWidgetItems из TreeWidget в виде:
    # {treeWidgetItem_index: {supplier_name: price_file_path}, ..., n}
    def __get_values_from_tree_widget_items(self) -> dict:
        root = self.ui.manual_parser_tree_widget.invisibleRootItem()
        item_index_sup_file_dict: dict = {}
        for item_index in range(root.childCount()):
            tree_widget_item = root.child(item_index)
            self.__convert_combobox_to_text(tree_widget_item, 2)
            item_index_sup_file_dict[item_index] = self.__get_values_from_tree_widget_item(tree_widget_item)
        return item_index_sup_file_dict

    # Возвращает значения из конкретного TreeWidgetItem
    @staticmethod
    def __get_values_from_tree_widget_item(tree_widget_item: QTreeWidgetItem) -> dict:
        dir_path: str = tree_widget_item.text(0)
        filename: str = tree_widget_item.text(1)
        supplier_name: str = tree_widget_item.text(2)
        file_path: str = dir_path + '\\' + filename
        return {supplier_name: file_path}

    # Превращает combobox в простое текстовое поле(ячейку)
    def __convert_combobox_to_text(self, tree_widget_item: QTreeWidgetItem, column: int):
        if isinstance(self.ui.manual_parser_tree_widget.itemWidget(tree_widget_item, column), QComboBox):
            combobox_value = self.ui.manual_parser_tree_widget.itemWidget(tree_widget_item, column).currentText()
            self.ui.manual_parser_tree_widget.removeItemWidget(tree_widget_item, column)
            tree_widget_item.setText(column, combobox_value)

    # Устанавливает цвет для treeWidgetItem
    def __set_tree_widget_item_color(self, item_index: int, color_hex: str):
        color = QColor(color_hex)
        self.ui.manual_parser_tree_widget.invisibleRootItem().child(item_index).setBackground(0, color)
        self.ui.manual_parser_tree_widget.invisibleRootItem().child(item_index).setBackground(1, color)
        self.ui.manual_parser_tree_widget.invisibleRootItem().child(item_index).setBackground(2, color)

    # При окончанию парсинга - спрашивает, открыть ли папку с результатом
    def on_result_ready_show_message(self):
        Speaker().show_message_on_result_ready(self.ui.result_path_parser_line_edit.text())

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
        # self.on_result_ready_show_message()

    # THREAD SLOTS AUTOMATIC PARSER
    def on_automatic_parser_started(self, supplier_name: str):
        self.__set_status_line_edits(supplier_name, config.QLINEEDIT_STYLE_PROCESSING_COLOR)
        self.__set_push_buttons_availability(supplier_name, False)

    def on_automatic_parser_finished(self, supplier_name: str):
        self.__set_status_line_edits(supplier_name, config.QLINEEDIT_STYLE_READY_COLOR)
        self.__set_push_buttons_availability(supplier_name, True)
        self.thread_auto_parser.quit()

    def __set_status_line_edits(self, supplier_name: str, color: str):
        automatic_parsing_line_edits: dict = {config.KVT_NAME: lambda: self.ui.link_kvt_line_edit.setStyleSheet(color),
                                              config.TORG7_NAME: lambda: self.ui.link_torg7_line_edit.setStyleSheet(
                                                  color),
                                              config.A4_NAME: lambda: self.ui.link_a4_line_edit.setStyleSheet(color)}
        return automatic_parsing_line_edits[supplier_name]()

    def __set_push_buttons_availability(self, supplier_name: str, status: bool):
        automatic_parsing_line_edits: dict = {config.KVT_NAME: lambda: self.ui.parse_kvt_push_button.setEnabled(status),
                                              config.TORG7_NAME: lambda: self.ui.parse_torg7_push_button.setEnabled(
                                                  status),
                                              config.A4_NAME: lambda: self.ui.parse_a4_push_button.setEnabled(status)}
        return automatic_parsing_line_edits[supplier_name]()

    def on_automatic_parsing_error(self, supplier_name: str, msg: str):
        self.thread_auto_parser.quit()
        self.__set_status_line_edits(supplier_name, config.QLINEEDIT_STYLE_ERROR_COLOR)
        self.__set_push_buttons_availability(supplier_name, True)
        Speaker().show_message_on_parsing_error(msg)

    def on_manual_parsing_error(self, item_index: int, msg: str):
        self.thread_manual_parser.quit()
        self.__set_tree_widget_item_color(item_index, config.STATUS_ERROR_COLOR)
        Speaker().show_message_on_parsing_error(msg)

    @staticmethod
    def test():
        print(123)
