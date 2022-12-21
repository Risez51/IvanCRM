import os.path
import pythoncom
from PyQt5 import QtCore
from controllers import view_config as vc
from actions.passport_protection import PassportProtection
from actions.supplier_parser import SupplierParser



class Worker(QtCore.QObject):
    # passport protection signals
    passport_protection_completed = QtCore.pyqtSignal()
    file_protection_started = QtCore.pyqtSignal(int, str)
    file_protection_finished = QtCore.pyqtSignal(int, str)

    # supplier parser signals
    supplier_parser_item_started = QtCore.pyqtSignal(int)
    supplier_parser_item_finished = QtCore.pyqtSignal(int)
    supplier_parser_finished = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        self.output_path = ''
        self.files = {}
        super().__init__(parent)

    def run_passport_protection(self):
        pythoncom.CoInitialize()

        for key, value in self.files.items():
            self.file_protection_started.emit(key, vc.STATUS_PROCESSING)
            dir_path = os.path.dirname(value)
            filename = os.path.basename(value)
            PassportProtection(dir_path,
                               self.output_path).start_one(filename)
            self.file_protection_finished.emit(key, vc.STATUS_READY)
        self.passport_protection_completed.emit()

    def run_supplier_parser(self):
        supplier_parser = SupplierParser(self.output_path)
        for item_index, file_dict in self.files.items():
            self.supplier_parser_item_started.emit(item_index)
            for supplier_name, file_path in file_dict.items():
                if supplier_name == 'КВТ_СИТ':
                    supplier_parser.create_kvt(file_path)
                elif supplier_name == 'Н1_ИД':
                    pass
                elif supplier_name == 'П1_ИД':
                    supplier_parser.create_p1(file_path)
                elif supplier_name == 'Торг2_ЧК':
                    supplier_parser.create_torg2(file_path)
                elif supplier_name == 'Торг7_ЧК':
                    pass
                elif supplier_name == 'Ю1_ИД':
                    supplier_parser.create_yu1(file_path)

                self.supplier_parser_item_finished.emit(item_index)
        self.supplier_parser_finished.emit()

    def set_params(self, files: dict, output_path: str):
        self.files = files
        self.output_path = output_path

