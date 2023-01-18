import main_window
from PyQt5 import QtCore

from orders.manual_parser_order import ManualParserOrder
from workers.manual_parser_worker import ManualParserWorker
from workers.auto_parser_worker import AutoParserWorker
from configs import config
from handlers.filedialog import FileDialog
from handlers.speaker import Speaker
from handlers.manual_parser_orders_handler import ManualParserOrdersHandler


class ParserController:
    def __init__(self, ui: main_window.Ui_MainWindow):
        self.ui = ui
        # Thread manual parser
        self.thread_manual_parser = QtCore.QThread()
        self.manual_worker = ManualParserWorker()
        self.manual_worker.moveToThread(self.thread_manual_parser)
        # Thread automatic parser
        self.thread_auto_parser = QtCore.QThread()
        self.auto_worker = AutoParserWorker()
        self.auto_worker.moveToThread(self.thread_auto_parser)
        # Thread manual connectors
        self.manual_worker.manual_suppler_parser_started.connect(self.on_manual_supplier_parser_started)
        self.manual_worker.manual_supplier_parser_item_started.connect(self.on_manual_supplier_parser_item_started)
        self.manual_worker.manual_supplier_parser_item_finished.connect(self.on_manual_supplier_parser_item_finished)
        self.manual_worker.manual_supplier_parser_finished.connect(self.on_manual_supplier_parser_finished)
        self.manual_worker.manual_supplier_parser_error.connect(self.on_manual_parsing_error)
        self.thread_manual_parser.started.connect(self.manual_worker.run)
        # Thread automatic connectors
        self.auto_worker.automatic_supplier_parser_started.connect(self.on_automatic_parser_started)
        self.auto_worker.automatic_supplier_parser_finished.connect(self.on_automatic_parser_finished)
        self.auto_worker.automatic_supplier_parser_error.connect(self.on_automatic_parsing_error)
        self.thread_auto_parser.started.connect(self.auto_worker.run)
        # GUI element connectors manual parser
        ui.add_price_push_button.clicked.connect(self.on_add_price_push_button)
        ui.delete_price_push_button.clicked.connect(self.on_delete_price_push_button)
        ui.start_parsing_push_button.clicked.connect(self.on_start_parsing_push_button)
        ui.add_result_path_parser_push_button.clicked.connect(self.on_add_result_path_parser_push_button)
        ui.add_multiple_price_push_button.clicked.connect(self.on_add_multiple_price_push_button)
        # GUI element connectors automatic parser
        ui.parse_kvt_push_button.clicked.connect(self.on_parse_kvt_push_button)
        ui.parse_torg7_push_button.clicked.connect(self.on_parse_torg7_push_button)
        ui.parse_a4_push_button.clicked.connect(self.on_parse_a4_push_button)
        # ParserOrdersHandler
        self.manual_orders_handler = ManualParserOrdersHandler(self.ui.manual_parser_tree_widget)
        # TEST
        ui.test_push_button.clicked.connect(self.test)

    # MANUAL PARSER ELEMENTS+++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Добавлет в TreeWidgetItem для 1 файла
    def on_add_price_push_button(self):
        files_location: list[str] = FileDialog().get_file_names()
        if files_location:
            for file_location in files_location:
                self.manual_orders_handler.new_order(file_location)

    # Добавлет в TreeWidgetItem для нескольких файлов
    def on_add_multiple_price_push_button(self):
        file_locations: list[str] = FileDialog().get_file_names()
        if file_locations:
            self.manual_orders_handler.new_order(file_locations)

    # Удаляет выбранный TreeWidgetItem
    def on_delete_price_push_button(self):
        self.manual_orders_handler.remove_selected_order()

    # Заполняет поле "Результирующий путь"
    def on_add_result_path_parser_push_button(self):
        specified_dir: str = FileDialog().get_dir_path()
        if specified_dir:
            self.ui.result_path_parser_line_edit.setText(specified_dir)

    # Start parsing files
    def on_start_parsing_push_button(self):
        if self.ui.manual_parser_tree_widget.invisibleRootItem().childCount() > 0 and \
                self.ui.result_path_parser_line_edit.text() != '':
            output_dir: str = self.ui.result_path_parser_line_edit.text()
            self.manual_worker.set_params(self.manual_orders_handler.get_orders(), output_dir)
            self.thread_manual_parser.start()
    # MANUAL PARSER ELEMENTS----------------------------------------------------

    # AUTOMATIC PARSER ELEMENTS+++++++++++++++++++++++++++++++++++++++++++++++++
    def on_parse_a4_push_button(self):
        if self.ui.result_path_parser_line_edit.text() != '':
            link: str = self.ui.link_a4_line_edit.text()
            output_path: str = self.ui.result_path_parser_line_edit.text()
            self.auto_worker.set_params(config.A4_NAME, link, output_path)
            self.thread_auto_parser.start()

    def on_parse_kvt_push_button(self):
        if self.ui.result_path_parser_line_edit.text() != '':
            link: str = self.ui.link_kvt_line_edit.text()
            output_path: str = self.ui.result_path_parser_line_edit.text()
            self.auto_worker.set_params(config.KVT_NAME, link, output_path)
            self.thread_auto_parser.start()

    def on_parse_torg7_push_button(self):
        if self.ui.result_path_parser_line_edit.text() != '':
            link: str = self.ui.link_torg7_line_edit.text()
            output_path: str = self.ui.result_path_parser_line_edit.text()
            self.auto_worker.set_params(config.TORG7_NAME, link, output_path)
            self.thread_auto_parser.start()

    # AUTOMATIC PARSER ELEMENTS------------------------------------------------

    # При окончанию парсинга - спрашивает, открыть ли папку с результатом
    def on_result_ready_show_message(self):
        Speaker().show_message_on_result_ready(self.ui.result_path_parser_line_edit.text())

    # THREAD SLOTS MANUAL PARSING+++++++++++++++++++++++++++++++++++++++
    # On started manual parsing
    def on_manual_supplier_parser_started(self):
        self.ui.start_parsing_push_button.setEnabled(False)
        self.ui.delete_price_push_button.setEnabled(False)
        self.ui.add_result_path_parser_push_button.setEnabled(False)
        self.ui.add_price_push_button.setEnabled(False)

    # On started manual parsing supplier_price changing color(status)
    def on_manual_supplier_parser_item_started(self, order: ManualParserOrder):
        self.manual_orders_handler.set_order_status(order, config.STATUS_PROCESSING_COLOR)

    # On finished manual parsing supplier_price changing color(status)
    def on_manual_supplier_parser_item_finished(self, order: ManualParserOrder):
        self.manual_orders_handler.set_order_status(order, config.STATUS_READY_COLOR)

    # On finished manual parsing all supplier_prices
    def on_manual_supplier_parser_finished(self):
        self.ui.add_result_path_parser_push_button.setEnabled(True)
        self.ui.delete_price_push_button.setEnabled(True)
        self.ui.start_parsing_push_button.setEnabled(True)
        self.ui.add_price_push_button.setEnabled(True)
        self.thread_manual_parser.quit()
        # self.on_result_ready_show_message()

    # On shows a message that an error occurred while trying to process the price
    def on_manual_parsing_error(self, order: ManualParserOrder, msg: str):
        self.thread_manual_parser.quit()
        self.manual_orders_handler.set_order_status(order, config.STATUS_ERROR_COLOR)
        Speaker().show_message_on_parsing_error(msg)
    # THREAD SLOTS MANUAL PARSING---------------------------------------

    # THREAD SLOTS AUTOMATIC PARSING+++++++++++++++++++++++++++++++++++++
    # Устанавливает цвет конкретного line_edit при запуске парсинга выбранного поставщика
    # Делает кнопку поставщика неактивной
    def on_automatic_parser_started(self, supplier_name: str):
        self.__set_status_line_edits(supplier_name, config.QLINEEDIT_STYLE_PROCESSING_COLOR)
        self.__set_push_buttons_availability(supplier_name, False)

    # Устанавливает цвет конкретного line_edit при окончание парсинга выбранного поставщика
    # Делает кнопку поставщика активной
    def on_automatic_parser_finished(self, supplier_name: str):
        self.__set_status_line_edits(supplier_name, config.QLINEEDIT_STYLE_READY_COLOR)
        self.__set_push_buttons_availability(supplier_name, True)
        self.thread_auto_parser.quit()

    # Срабатывает, если не удалось обработать выбранного поставщика
    def on_automatic_parsing_error(self, supplier_name: str, msg: str):
        self.thread_auto_parser.quit()
        self.__set_status_line_edits(supplier_name, config.QLINEEDIT_STYLE_ERROR_COLOR)
        self.__set_push_buttons_availability(supplier_name, True)
        Speaker().show_message_on_parsing_error(msg)
    # THREAD SLOTS AUTOMATIC PARSING------------------------------------

    # Change status for auto parsing gui widgets
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

    def test(self):
        pass