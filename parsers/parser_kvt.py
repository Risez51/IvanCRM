from parsers import parsing_parameters as pp
from file_manager.storage import Storage
import pandas as pd
from parsers.result_dataframe import ResultDataFrame


class ParserKVT(ResultDataFrame):
    def __init__(self, file_path: str):
        super().__init__()
        # ВРЕМЕННО ПОЛУЧАЮ ФАЙЛ ПО ССЫЛКЕ С САЙТА
        # ТРЕБУЕТСЯ РЕАЛИЗОВАТЬ ВАРИАЦИЮ ССЫЛКА/КОНКРЕТНЫЙ ФАЙЛ
        self.__df_stock = Storage().get_dataframe(file_path, start_row=1)

    def get_result(self) -> pd.DataFrame:
        self.normalize_dataframe()
        self.__fill_frame()
        return self.get_result_dataframe()

    def __fill_frame(self):
        self.set_article(self.__df_stock['код товара'])
        self.set_name(self.__df_stock['Наименование'])
        self.set_unit(self.__df_stock['ед.изм.'])
        self.set_purchase_price((self.__df_stock['РРЦ'] / pp.NDS).round(2))
        self.set_quantity(self.__df_stock['на складе (кол-во)'])
        self.set_selling_price(self.get_purchase_price())
        self.set_site_name(self.__df_stock['Наименование'])

    def normalize_dataframe(self):
        self.__df_stock.dropna(axis=0,
                               subset=['код товара',
                                       'Наименование',
                                       'на складе (кол-во)',
                                       'РРЦ'],
                               inplace=True)
        self.__df_stock['на складе (кол-во)'] = pd.to_numeric(self.__df_stock['на складе (кол-во)'])
        self.__df_stock.loc[(self.__df_stock['на складе (кол-во)'] > 1_000_000), 'на складе (кол-во)'] = 100_000
