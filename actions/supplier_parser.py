from parsers import parser_a4, parser_torg7, parser_kvt
from file_manager.storage import Storage
from datetime import datetime


class SupplierParser:

    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        self.today = datetime.today().strftime('%d-%m-%y')

    def create_all(self):
        self.create_a4()
        self.create_kvt()
        self.create_torg7()

    def create_a4(self):
        dataframe = parser_a4.ParserA4().get_result()
        filename = f"{self.output_dir}\\А4_ИД от {self.today}.xlsx"
        self.__create_chk_file(dataframe, filename)

    def create_kvt(self):
        dataframe = parser_kvt.ParserKVT().get_result()
        filename = f"{self.output_dir}\\КВТ_СИТ от {self.today}.xlsx"
        self.__create_chk_file(dataframe, filename)

    def create_torg7(self):
        dataframe = parser_torg7.ParserTorg7().get_result()
        filename = f"{self.output_dir}\\Торг7_ЧК от {self.today}.xlsx"
        self.__create_chk_file(dataframe, filename)

    @staticmethod
    def __create_chk_file(data, filename):
        Storage().to_excel(data, filename)
        filename_chk = Storage().replace_xl_to_chk(filename)
        Storage().rename(filename, filename_chk)
