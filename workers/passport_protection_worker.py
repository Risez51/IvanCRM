import pythoncom
from PyQt5 import QtCore
from actions.passport_protection import PassportProtection
from configs import config
from orders.passport_protection_order import PassportProtectionOrder
"""
Данный класс отправляется в поток и совершает работу по:
 - Защита паспортов 
"""


class PassportProtectionWorker(QtCore.QObject):
    # passport protection signals
    # Сигнал, что начата обработка конкретного файла
    passport_protection_started = QtCore.pyqtSignal(PassportProtectionOrder, str, str)
    # Сигнал, что обработка конкретного файла завершена
    passport_protection_finished = QtCore.pyqtSignal(PassportProtectionOrder, str, str)
    # Сигнал, что завершена обработка всех файлов
    passport_protection_completed = QtCore.pyqtSignal()
    # --------------------------------------------------
    # Путь, где будет создана папка с обработанными файлами
    __output_path: str
    # Список заявок
    __orders: list[PassportProtectionOrder]

    def __init__(self, parent=None):
        super().__init__(parent)

    # Создает защищенные паспорта из TreeWidgetItems, указанных в TreeWidget (title == Защита паспортов)
    def run(self):
        # Инициализация COMObject
        pythoncom.CoInitialize()
        for order in self.__orders:
            self.passport_protection_started.emit(order, config.STATUS_PROCESSING_COLOR, config.STATUS_PROCESSING)
            PassportProtection(order.get_file_dir(),
                               self.__output_path).create_protected_passport(order.get_file_name())
            self.passport_protection_finished.emit(order, config.STATUS_READY_COLOR, config.STATUS_READY)
        self.passport_protection_completed.emit()

    def set_params(self, files: list[PassportProtectionOrder], output_dir: str):
        self.__orders = files
        self.__output_path = output_dir
