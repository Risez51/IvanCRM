import os.path
import pythoncom
from PyQt5 import QtCore
from file_manager.storage import Storage
from actions.passport_protection import PassportProtection
from actions.supplier_parser import SupplierParser
from configs import config

"""
Данный класс отправляется в поток и совершает работу по:
 1. Защита паспортов ( run_passport_protection )
 2. Ручной парсинг прайс-листов ( run_manual_supplier_parsing )
 3. Автоматический парсинг прайс-листов ( run_automatic_supplier_parsing )
 Ручная обработка, отличается от автоматической, тем, что не нужно добавлять в TreeWidget
 отдельные items для указания файла и поставщика. Запускается по отдельной кнопке(своя для каждого из поставщиков,
 которых можно парсить по ссылке (url)).
"""


class Worker(QtCore.QObject):
    # passport protection signals
    # Сигнал, что начата обработка конкретного файла
    file_protection_started = QtCore.pyqtSignal(int, str)
    # Сигнал, что обработка конкретного файла завершена
    file_protection_finished = QtCore.pyqtSignal(int, str)
    # Сигнал, что завершена обработка всех файлов
    passport_protection_completed = QtCore.pyqtSignal()
    # ---------------------------------------------------------------------------------
    # manual supplier parser signals
    # Сигнал, что ручной парсинг запущен
    manual_suppler_parser_started = QtCore.pyqtSignal()
    # Сигнал, что запущен парсинг конкретного поставщика (указанного в TreeWidgetItem)
    manual_supplier_parser_item_started = QtCore.pyqtSignal(int)
    # Сигнал, что окончен парсинг конкретного поставщика (указанного в TreeWidgetItem)
    manual_supplier_parser_item_finished = QtCore.pyqtSignal(int)
    # Сигнал, что ручной парсинг завершен
    manual_supplier_parser_finished = QtCore.pyqtSignal()
    # Сигнал, что произошла ошибка при парсинге конкретного поставщика
    manual_supplier_parser_error = QtCore.pyqtSignal(int, str)
    # ---------------------------------------------------------------------------------
    # automatic supplier parser signals
    # Сигнал, что автоматический парсинг поставщика запущен
    automatic_supplier_parser_started = QtCore.pyqtSignal(str)
    # Сигнал, что автоматический парсинг поставщика завершен
    automatic_supplier_parser_finished = QtCore.pyqtSignal(str)
    # Сигнал, что произошла ошибка при автоматическом парсинге поставщика
    automatic_supplier_parser_error = QtCore.pyqtSignal(str, str)

    def __init__(self, parent=None):
        self.__output_path = ''
        self.__files = {}
        self.__supplier_name = ''
        self.__file_location = ''
        super().__init__(parent)

    # Создает защищенные паспорта из TreeWidgetItems, указанных в TreeWidget (title == Защита паспортов)
    def run_passport_protection(self):
        # Инициализация COMObject
        pythoncom.CoInitialize()
        # self.__files == {TreeWidgetItemIndex: file_location}
        for item_index, file_location in self.__files.items():
            self.file_protection_started.emit(item_index, config.STATUS_PROCESSING)
            dir_path = os.path.dirname(file_location)
            filename = os.path.basename(file_location)
            PassportProtection(dir_path, self.__output_path).create_protected_passport(filename)
            self.file_protection_finished.emit(item_index, config.STATUS_READY)
        self.passport_protection_completed.emit()

    # Ручная обработка файлов (через добавление items в TreeWidget)
    def run_manual_supplier_parser(self):
        self.manual_suppler_parser_started.emit()
        # self.__files == {TreeWidgetItemIndex: {supplier_name: file_location}, ..., n}
        for item_index, file_dict in self.__files.items():
            self.manual_supplier_parser_item_started.emit(item_index)
            for supplier_name, file_location in file_dict.items():
                try:
                    self.__create_parsed_chk_file(supplier_name, file_location, self.__output_path)
                    self.manual_supplier_parser_item_finished.emit(item_index)
                except Exception as e:
                    self.manual_supplier_parser_error.emit(item_index,
                                                           supplier_name + '\n' + file_location + '\n' + str(e))
        self.manual_supplier_parser_finished.emit()

    # Автоматическая обработка файлов (При нажатие на кнопку спарсить %имя поставщика%)
    def run_automatic_supplier_parser(self):
        self.automatic_supplier_parser_started.emit(self.__supplier_name)
        try:
            self.__create_parsed_chk_file(self.__supplier_name, self.__file_location, self.__output_path)
            self.automatic_supplier_parser_finished.emit(self.__supplier_name)
        except Exception as e:
            self.automatic_supplier_parser_error.emit(self.__supplier_name, self.__supplier_name + '\n' + str(e))

    # Задает параметры для автоматического парсинга, в аргументах название поставщика, ссылка на прайс,
    # как правило url (но может и в локальную), путь, где будет создан результирующай файл
    def set_automatic_parser_params(self, supplier_name: str, supplier_link: str,  output_path: str):
        self.__output_path = output_path
        self.__supplier_name = supplier_name
        self.__file_location = supplier_link

    # Задает параметры для ручного парсинга, где files == {TreeWidgetItemIndex: {supplier_name: file_location}, ..., n}
    # output_path == путь, где будут храниться результирующие файлы
    def set_manual_parser_params(self, files: dict, output_path: str):
        self.__files = files
        self.__output_path = output_path

    # Принимает в аргументы имя поставщика, расположение файла, путь, где будет создан результирующий файл
    # -> Парсит файл -> Создает имя файла -> Создает .chk файл в output_dir
    @staticmethod
    def __create_parsed_chk_file(supplier_name: str, file_location: str, output_path: str):
        # Получение спарсенного и обработанного датафрейма
        parsed_data = SupplierParser().get_parsed_dataframe(supplier_name, file_location)
        # Создает имя для результирующего файла
        parsed_file_name = Storage().get_supplier_file_name(supplier_name)
        # Конкантенация пути с результатом и имени файла
        parsed_file_output_location = output_path + parsed_file_name
        # Создает результирующий файл
        Storage().to_chk(parsed_data, parsed_file_output_location)
