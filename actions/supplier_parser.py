from parsers import parser_a4, parser_torg7, parser_kvt, parser_torg2, parser_yu1_id, parser_p1_id, parser_n1_id
from file_manager.storage import Storage
from datetime import datetime


class SupplierParser:

    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        self.today = datetime.today().strftime('%d-%m-%y')

    # def create_all(self):
    #     self.create_a4()
    #     self.create_kvt()
    #     self.create_torg7()

    def create_a4(self, file_path: str):
        dataframe = parser_a4.ParserA4(file_path).get_result()
        filename = f"{self.output_dir}\\А4_ИД от {self.today}.xlsx"
        self.__create_chk_file(dataframe, filename)

    def create_kvt(self, file_path: str):
        dataframe = parser_kvt.ParserKVT(file_path).get_result()
        filename = f"{self.output_dir}\\КВТ_СИТ от {self.today}.xlsx"
        self.__create_chk_file(dataframe, filename)

    def create_torg7(self, file_path: str):
        dataframe = parser_torg7.ParserTorg7(file_path).get_result()
        filename = f"{self.output_dir}\\Торг7_ЧК от {self.today}.xlsx"
        self.__create_chk_file(dataframe, filename)

    def create_torg2(self, file_path: str):
        dataframe = parser_torg2.ParserTorg2(file_path).get_result()
        filename = f"{self.output_dir}\\Торг2_ЧК от {self.today}.xlsx"
        self.__create_chk_file(dataframe, filename)

    def create_yu1(self, file_path: str):
        dataframe = parser_yu1_id.ParserYu1(file_path).get_result()
        filename = f"{self.output_dir}\\Ю1_ИД от {self.today}.xlsx"
        self.__create_chk_file(dataframe, filename)

    def create_p1(self, file_path: str):
        dataframe = parser_p1_id.ParserP1(file_path).get_result()
        filename = f"{self.output_dir}\\П1_ИД от {self.today}.xlsx"
        self.__create_chk_file(dataframe, filename)

    def create_n1(self, files_list: list):
        dataframe = parser_n1_id.ParserN1(files_list).get_result()
        filename = f"{self.output_dir}\\Н1_ИД от {self.today}.xlsx"
        self.__create_chk_file(dataframe, filename)

    @staticmethod
    def __create_chk_file(data, filename):
        Storage().to_excel(data, filename)
        filename_chk = Storage().replace_xl_to_chk(filename)
        Storage().rename(filename, filename_chk)
