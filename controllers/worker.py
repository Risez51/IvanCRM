import os.path

import pythoncom
from PyQt5 import QtCore
from actions.passport_protection import PassportProtection

#Сразу перед инициализацией DCOM в run()


class Worker(QtCore.QObject):
    # passport protection signals
    passport_protection_completed = QtCore.pyqtSignal()
    file_protection_started = QtCore.pyqtSignal(int, str)
    file_protection_finished = QtCore.pyqtSignal(int, str)

    def __init__(self, parent=None):
        self.output_path = ''
        self.files = {}
        super().__init__(parent)

    def run_passport_protection(self):
        pythoncom.CoInitialize()

        for key, value in self.files.items():
            self.file_protection_started.emit(key, f'Обрабатывается')
            dir_path = os.path.dirname(value)
            filename = os.path.basename(value)
            PassportProtection(dir_path,
                               self.output_path).start_one(filename)
            self.file_protection_finished.emit(key, f'Готов')
        self.passport_protection_completed.emit()

    def set_params(self, files: dict, output_path: str):
        self.files = files
        self.output_path = output_path

