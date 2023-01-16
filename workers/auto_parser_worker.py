from PyQt5 import QtCore
from file_manager.storage import Storage
from actions.supplier_parser import SupplierParser

"""
Данный класс отправляется в поток и совершает работу по:
 - Автоматический парсинг прайс-листов 
"""


class AutoParserWorker(QtCore.QObject):
    # automatic supplier parser signals
    # Сигнал, что автоматический парсинг поставщика запущен
    automatic_supplier_parser_started = QtCore.pyqtSignal(str)
    # Сигнал, что автоматический парсинг поставщика завершен
    automatic_supplier_parser_finished = QtCore.pyqtSignal(str)
    # Сигнал, что произошла ошибка при автоматическом парсинге поставщика
    automatic_supplier_parser_error = QtCore.pyqtSignal(str, str)

    def __init__(self, parent=None):
        self.__output_path = ''
        self.__supplier_name = ''
        self.__file_location = []
        super().__init__(parent)

    # Автоматическая обработка файлов (При нажатие на кнопку спарсить %имя поставщика%)
    def run(self):
        self.automatic_supplier_parser_started.emit(self.__supplier_name)
        try:
            self.__create_parsed_chk_file(self.__supplier_name, self.__file_location, self.__output_path)
            self.automatic_supplier_parser_finished.emit(self.__supplier_name)
        except Exception as e:
            self.automatic_supplier_parser_error.emit(self.__supplier_name, self.__supplier_name + '\n' + str(e))

    # Задает параметры для автоматического парсинга, в аргументах название поставщика, ссылка на прайс,
    # как правило url (но может и в локальную), путь, где будет создан результирующай файл
    def set_params(self, supplier_name: str, supplier_link: str, output_path: str):
        self.__file_location.clear()
        self.__supplier_name = supplier_name
        self.__file_location.append(supplier_link)
        self.__output_path = output_path

    # Принимает в аргументы имя поставщика, расположение файла, путь, где будет создан результирующий файл
    # -> Парсит файл -> Создает имя файла -> Создает .chk файл в output_dir
    @staticmethod
    def __create_parsed_chk_file(supplier_name: str, file_location: list[str], output_path: str):
        # Получение спарсенного и обработанного датафрейма
        parsed_data = SupplierParser().get_parsed_dataframe(supplier_name, file_location)
        # Создает имя для результирующего файла
        parsed_file_name = Storage().get_supplier_file_name(supplier_name)
        # Конкантенация пути с результатом и имени файла
        parsed_file_output_location = output_path + parsed_file_name
        # Создает результирующий файл
        Storage().to_chk(parsed_data, parsed_file_output_location)
