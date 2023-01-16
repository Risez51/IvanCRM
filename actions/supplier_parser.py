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
    @staticmethod
    def get_parsed_dataframe(supplier_name: str, files: list[str]):
        parsers = {config.A4_NAME: lambda: ParserA4(files).get_result(),
                   config.TORG2_NAME: lambda: ParserTorg2(files).get_result(),
                   config.TORG7_NAME: lambda: ParserTorg7(files).get_result(),
                   config.KVT_NAME: lambda: ParserKVT(files).get_result(),
                   config.N1_NAME: lambda: ParserN1(files).get_result(),
                   config.YU1_NAME: lambda: ParserYu1(files).get_result(),
                   config.P1_NAME: lambda: ParserP1(files).get_result(),
                   }
        return parsers[supplier_name]()
