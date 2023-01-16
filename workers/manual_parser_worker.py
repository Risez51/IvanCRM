from PyQt5 import QtCore
from orders.manual_parser_order import ManualParserOrder
from file_manager.storage import Storage
from actions.supplier_parser import SupplierParser
"""
Данный класс отправляется в поток и совершает работу по:
 - Ручной парсинг прайс-листов
 Ручная обработка, отличается от автоматической, тем, что не нужно добавлять в TreeWidget
 отдельные items для указания файла и поставщика. Запускается по отдельной кнопке(своя для каждого из поставщиков,
 которых можно парсить по ссылке (url)).
"""


class ManualParserWorker(QtCore.QObject):
    # manual supplier parser signals
    # Сигнал, что ручной парсинг запущен
    manual_suppler_parser_started = QtCore.pyqtSignal()
    # Сигнал, что запущен парсинг конкретного поставщика (указанного в TreeWidgetItem)
    manual_supplier_parser_item_started = QtCore.pyqtSignal(ManualParserOrder)
    # Сигнал, что окончен парсинг конкретного поставщика (указанного в TreeWidgetItem)
    manual_supplier_parser_item_finished = QtCore.pyqtSignal(ManualParserOrder)
    # Сигнал, что ручной парсинг завершен
    manual_supplier_parser_finished = QtCore.pyqtSignal()
    # Сигнал, что произошла ошибка при парсинге конкретного поставщика
    manual_supplier_parser_error = QtCore.pyqtSignal(ManualParserOrder, str)
    # ---------------------------------------------------------------------------------
    # Путь, где будут созданы спрасенные и конвертированные файлы
    __output_path: str
    # Список заявок
    __orders: list[ManualParserOrder]

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        self.manual_suppler_parser_started.emit()
        for order in self.__orders:
            self.manual_supplier_parser_item_started.emit(order)
            try:
                self.__create_parsed_chk_file(order.get_supplier_name(),
                                              order.get_files(),
                                              self.__output_path)
                self.manual_supplier_parser_item_finished.emit(order)
            except Exception as e:
                self.manual_supplier_parser_error.emit(order,
                                                       order.get_supplier_name() +
                                                       '\n' + order.get_supplier_name() +
                                                       '\n' + str(e))
        self.manual_supplier_parser_finished.emit()

    # Задает параметры для ручного парсинга
    # output_path == путь, где будут храниться результирующие файлы
    def set_params(self, orders: list[ManualParserOrder], output_path: str):
        self.__orders = orders
        self.__output_path = output_path

    # Принимает в аргументы имя поставщика, расположение файла, путь, где будет создан результирующий файл
    # -> Парсит файл -> Создает имя файла -> Создает .chk файл в output_dir
    @staticmethod
    def __create_parsed_chk_file(supplier_name: str, files_location: list[str], output_path: str):
        # Получение спарсенного и обработанного датафрейма
        parsed_data = SupplierParser().get_parsed_dataframe(supplier_name, files_location)
        # Создает имя для результирующего файла
        parsed_file_name = Storage().get_supplier_file_name(supplier_name)
        # Конкантенация пути с результатом и имени файла
        parsed_file_output_location = output_path + parsed_file_name
        # Создает результирующий файл
        Storage().to_chk(parsed_data, parsed_file_output_location)
