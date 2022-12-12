from parsers import parsing_parameters as pp
from parsers.result_dataframe import ResultDataFrame
from file_manager.storage import Storage
import pandas as pd


class ParserP1(ResultDataFrame):
    def __init__(self):
        super().__init__()
        path_with_prices = pp.LOCAL_PRICE_PATH + '/П1_ИД/'
        files_list = Storage().get_filenames(pp.LOCAL_PRICE_PATH + '/П1_ИД/')
        self.__df_stock = Storage().get_dataframe(path_with_prices + '/' + files_list[0])

    def get_result(self) -> pd.DataFrame:
        self.__normalize_dataframe()
        self.__fill_frame()
        return self.get_result_dataframe()

    def __fill_frame(self):
        self.set_article(self.__df_stock['Код'])
        self.set_name(self.__df_stock['Наименование'])
        self.set_purchase_price((self.__df_stock['Мин. Опт. Цена'] / pp.NDS).round(2))
        self.set_quantity(self.__df_stock['В свободной продаже'])
        self.set_brand(self.__df_stock['Бренд'])
        self.set_selling_price((self.get_purchase_price() * pp.P1_MARGIN).round(2))
        self.get_result_dataframe().loc[(self.get_purchase_price() < self.__df_stock['РЦ'] / pp.NDS),
                                        'Цена продажи, б/ндс'] = (self.__df_stock['РЦ'] / pp.NDS).round(2)
        self.set_site_name(self.__df_stock['Наименование'])
        self.set_multiplicity(self.__df_stock['Мин. кол-во к заказу/кратно'])

    def __normalize_dataframe(self):
        self.__df_stock.loc[(pd.to_numeric(self.__df_stock['В свободной продаже']) < 1), 'В свободной продаже'] = pd.NA
        self.__df_stock[
            ~self.__df_stock['Бренд'].str.contains('|'.join(pp.P1_NEEDFUL_BRANDS), na=False, case=False)] = pd.NA
        self.__df_stock.dropna(axis=0,
                               subset=['Код',
                                       'Наименование',
                                       'В свободной продаже',
                                       'Мин. Опт. Цена'],
                               inplace=True)
        self.__df_stock['Мин. Опт. Цена'] = pd.to_numeric(self.__df_stock['Мин. Опт. Цена'])
        self.__df_stock['РЦ'] = pd.to_numeric(self.__df_stock['РЦ'])
        self.__df_stock.loc[(self.__df_stock['В свободной продаже'] > 1_000_000), 'В свободной продаже'] = 100_000
