from parsers import parsing_parameters as pp
from file_manager.storage import Storage
import pandas as pd
from parsers.result_dataframe import ResultDataFrame


class ParserYu1(ResultDataFrame):
    def __init__(self, file_path):
        super().__init__()
        self.__df_stock = Storage().get_dataframe(file_path)

    def get_result(self) -> pd.DataFrame:
        self.normalize_dataframe()
        self.__fill_dataframe()
        return self.get_result_dataframe()

    def __fill_dataframe(self):
        self.set_article(self.__df_stock['Модификация'])
        self.set_name(self.__df_stock['Название'])
        self.set_unit(self.__df_stock['Ед.изм.'])
        self.set_purchase_price((self.__df_stock['ЦЕНА клиента'] / pp.NDS).round(2))
        self.set_quantity(self.__df_stock['Наличие'])
        self.set_brand(self.__df_stock['Торговая марка'])
        self.set_selling_price((self.__df_stock['ЦЕНА клиента'] / pp.NDS * pp.YU1_MARGIN).round(2))
        self.get_result_dataframe().loc[self.__df_stock['РРЦ'] > 0,
                                        'Цена продажи, б/ндс'] = (self.__df_stock['РРЦ'] / pp.NDS).round(2)
        self.set_site_name(self.__df_stock['Название'])
        self.set_multiplicity(self.__df_stock['Min кол-во отгрузки'])

    def normalize_dataframe(self):
        self.__df_stock[
            ~self.__df_stock['Торговая марка'].str.contains('|'.join(pp.YU1_NEEDFUL_BRANDS),
                                                            na=False,
                                                            case=False)] = pd.NA
        self.__df_stock.loc[(self.__df_stock['Наличие'] == '< 10'), 'Наличие'] = 9
        self.__df_stock.loc[(self.__df_stock['Наличие'] == '> 10'), 'Наличие'] = 15
        self.__df_stock.loc[(self.__df_stock['Наличие'] == '> 50'), 'Наличие'] = 60
        self.__df_stock.loc[(self.__df_stock['Наличие'] == '> 100'), 'Наличие'] = 150
        self.__df_stock.loc[(self.__df_stock['Наличие'] == '> 500'), 'Наличие'] = 600
        self.__df_stock.loc[(self.__df_stock['Наличие'] == '> 1000'), 'Наличие'] = 1100
        self.__df_stock.loc[(self.__df_stock['Наличие'] == 'нет'), 'Наличие'] = pd.NA
        self.__df_stock.loc[(self.__df_stock['РРЦ'] == ''), 'РРЦ'] = 0
        self.__df_stock.dropna(axis=0,
                               subset=['Торговая марка',
                                       'Модификация',
                                       'Название',
                                       'Наличие',
                                       'ЦЕНА клиента'],
                               inplace=True)
        self.__df_stock['РРЦ'] = pd.to_numeric(self.__df_stock['РРЦ'])
        self.__df_stock['ЦЕНА клиента'] = pd.to_numeric(self.__df_stock['ЦЕНА клиента'])
