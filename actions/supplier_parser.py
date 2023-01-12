import os

import pandas as pd

from parsers.parser_a4 import ParserA4
from parsers.parser_torg7 import ParserTorg7
from parsers.parser_kvt import ParserKVT
from parsers.parser_torg2 import ParserTorg2
from parsers.parser_yu1_id import ParserYu1
from parsers.parser_p1_id import ParserP1
from parsers.parser_n1_id import ParserN1

from configs import config

"""
 Класс для получения спарсенного файла/прайс-листа поставщика
 
"""


class SupplierParser:

    # Возвращает dataframe с результатом парсинга поставщика
    # В аргументах имя поставщика, расположение файла
    def get_parsed_dataframe(self, supplier_name: str, file_location):
        parsers = {config.A4_NAME: lambda: ParserA4(file_location).get_result(),
                   config.TORG2_NAME: lambda: ParserTorg2(file_location).get_result(),
                   config.TORG7_NAME: lambda: ParserTorg7(file_location).get_result(),
                   config.KVT_NAME: lambda: ParserKVT(file_location).get_result(),
                   config.N1_NAME: lambda: self.__get_result_dataframe_from_n1(file_location),
                   config.YU1_NAME: lambda: ParserYu1(file_location).get_result(),
                   config.P1_NAME: lambda: ParserP1(file_location).get_result(),
                   }
        return parsers[supplier_name]()

    # Возвращает dataframe, с результатом парсинга поставщика Н1_ИД (из 3-х файлов)
    def __get_result_dataframe_from_n1(self, files_location: str) -> pd.DataFrame:
        # Получение списка [file_location_1, ..., file_location_n]
        files = self.__get_files_list_for_multiple_parsing(files_location)
        # Парсинг поставщика Н1_ИД -> result dataframe
        dataframe = ParserN1(files).get_result()
        return dataframe

    # Функция, которая возвращает список файлов, для парсинга поставщиков, которые содержат несколько прайс-файлов
    # В аргументах строка "file_path\\file_name_1;file_name_2; ...;file_name_n;''"
    @staticmethod
    def __get_files_list_for_multiple_parsing(files_path: str):
        files_list = files_path.split(';')
        dir_path = os.path.dirname(files_list[0])
        files_list[0] = os.path.basename(files_list[0])
        return [dir_path + '\\' + file for file in files_list if file != '']
