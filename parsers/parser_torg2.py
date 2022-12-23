from parsers import parsing_parameters as pp
from parsers.result_dataframe import ResultDataFrame
from file_manager.storage import Storage
import pandas as pd


class ParserTorg2(ResultDataFrame):
    def __init__(self, file_path):
        super().__init__()
        self.__df_stock = Storage().get_dataframe(file_path, start_row=12)

    def get_result(self) -> pd.DataFrame:
        self.__normalize_dataframe()
        self.__fill_dataframe()
        return self.get_result_dataframe()

    def __fill_dataframe(self):
        self.set_name(self.__df_stock['Наименование'])
        self.set_unit(self.__df_stock['Ед. изм.'])
        self.set_purchase_price(self.__df_stock['Цена перечислением без НДС'])
        self.set_quantity(self.__df_stock['Количество'])
        self.set_selling_price(self.get_purchase_price() * pp.TORG2_MARGIN)
        self.set_site_name(self.__df_stock['Наименование'])

    def __normalize_dataframe(self):
        self.__df_stock.loc[(self.__df_stock['Цена перечислением без НДС'] == 'договор.'),
                            'Цена перечислением без НДС'] = pd.NA
        self.__df_stock[self.__df_stock['Наименование'].str.contains('|'.join(pp.TORG2_EXCEPTIONS_BRANDS),
                                                                     na=False, case=False)] = pd.NA
        self.__df_stock.dropna(axis=0,
                               subset=['артикул',
                                       'Наименование',
                                       'Количество',
                                       'Цена перечислением без НДС'],
                               inplace=True)
        self.__df_stock['Количество'] = pd.to_numeric(self.__df_stock['Количество'])
        self.__df_stock.loc[(self.__df_stock['Количество'] > 1_000_000), 'Количество'] = 100_000
