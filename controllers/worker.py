import os.path
import pythoncom
from PyQt5 import QtCore
from controllers import view_config as vc
from actions.passport_protection import PassportProtection
from actions.supplier_parser import SupplierParser
from controllers import view_config as vc


class Worker(QtCore.QObject):
    # passport protection signals
    passport_protection_completed = QtCore.pyqtSignal()
    file_protection_started = QtCore.pyqtSignal(int, str)
    file_protection_finished = QtCore.pyqtSignal(int, str)
    # manual supplier parser signals
    manual_suppler_parser_started = QtCore.pyqtSignal()
    manual_supplier_parser_item_started = QtCore.pyqtSignal(int)
    manual_supplier_parser_item_finished = QtCore.pyqtSignal(int)
    manual_supplier_parser_finished = QtCore.pyqtSignal()
    # automatic supplier parser signal
    automatic_supplier_parser_started = QtCore.pyqtSignal(str)
    automatic_supplier_parser_finished = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        self.output_path = ''
        self.files = {}
        self.supplier_name = ''
        self.supplier_link = ''
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

    def run_manual_supplier_parser(self):
        self.manual_suppler_parser_started.emit()
        supplier_parser = SupplierParser(self.output_path)
        for item_index, file_dict in self.files.items():
            self.manual_supplier_parser_item_started.emit(item_index)
            for supplier_name, file_path in file_dict.items():
                if supplier_name == vc.KVT_NAME:
                    supplier_parser.create_kvt(file_path)
                elif supplier_name == vc.N1_NAME:
                    files_list = self.get_files_list_for_multiple_parsing(file_path)
                    supplier_parser.create_n1(files_list)
                elif supplier_name == vc.P1_NAME:
                    supplier_parser.create_p1(file_path)
                elif supplier_name == vc.TORG2_NAME:
                    supplier_parser.create_torg2(file_path)
                elif supplier_name == vc.TORG7_NAME:
                    supplier_parser.create_torg7(file_path)
                elif supplier_name == vc.YU1_NAME:
                    supplier_parser.create_yu1(file_path)
                self.manual_supplier_parser_item_finished.emit(item_index)
        self.manual_supplier_parser_finished.emit()

    @staticmethod
    def get_files_list_for_multiple_parsing(file_path):
        files_list = file_path.split(';')
        dir_path = os.path.dirname(files_list[0])
        files_list[0] = os.path.basename(files_list[0])
        return [dir_path + '\\' + file for file in files_list if file != '']

    def run_automatic_supplier_parser(self):
        self.automatic_supplier_parser_started.emit(self.supplier_name)
        supplier_parser = SupplierParser(self.output_path)
        if self.supplier_name == vc.KVT_NAME:
            supplier_parser.create_kvt(self.supplier_link)
        elif self.supplier_name == vc.TORG7_NAME:
            supplier_parser.create_torg7(self.supplier_link)
        elif self.supplier_name == vc.A4_NAME:
            supplier_parser.create_a4(self.supplier_link)
        self.automatic_supplier_parser_finished.emit(self.supplier_name)

    def set_automatic_parser_params(self, supplier_name: str, supplier_link: str,  output_path: str):
        self.output_path = output_path
        self.supplier_name = supplier_name
        self.supplier_link = supplier_link

    def set_manual_parser_params(self, files: dict, output_path: str):
        self.files = files
        self.output_path = output_path

