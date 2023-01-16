from file_manager.storage import Storage
import pandas as pd
from parsers.result_dataframe import ResultDataFrame
from configs import config


class ParserYu1(ResultDataFrame):
    def __init__(self, files: list[str]):
        super().__init__()
        self.__df_stock = Storage().get_dataframe(files[0])
        self.headers = config.YU1_HEADERS

    def get_result(self) -> pd.DataFrame:
        self.normalize_dataframe()
        self.__fill_dataframe()
        return self.get_result_dataframe()

    def __fill_dataframe(self):
        self.set_article(self.__df_stock[self.headers.article])
        self.set_name(self.__df_stock[self.headers.name])
        self.set_unit(self.__df_stock[self.headers.unit])
        self.set_purchase_price((self.__df_stock[self.headers.purchase_price] / config.NDS).round(2))
        self.set_quantity(self.__df_stock[self.headers.quantity])
        self.set_brand(self.__df_stock[self.headers.brand])
        self.set_selling_price((self.__df_stock[self.headers.purchase_price] / config.NDS * config.YU1_MARGIN).round(2))
        self.get_result_dataframe().loc[self.__df_stock[self.headers.rrc] > 0,
                                        self.get_purchase_price_column_name()] = (self.__df_stock[self.headers.rrc]
                                                                                  / config.NDS).round(2)
        self.set_site_name(self.__df_stock[self.headers.name])
        self.set_multiplicity(self.__df_stock[self.headers.multiplicity])

    def normalize_dataframe(self):
        self.__df_stock[
            ~self.__df_stock[self.headers.brand].str.contains('|'.join(config.YU1_NEEDFUL_BRANDS),
                                                              na=False,
                                                              case=False)] = pd.NA
        self.__df_stock.loc[(self.__df_stock[self.headers.quantity] == '< 10'), self.headers.quantity] = 9
        self.__df_stock.loc[(self.__df_stock[self.headers.quantity] == '> 10'), self.headers.quantity] = 15
        self.__df_stock.loc[(self.__df_stock[self.headers.quantity] == '> 50'), self.headers.quantity] = 60
        self.__df_stock.loc[(self.__df_stock[self.headers.quantity] == '> 100'), self.headers.quantity] = 150
        self.__df_stock.loc[(self.__df_stock[self.headers.quantity] == '> 500'), self.headers.quantity] = 600
        self.__df_stock.loc[(self.__df_stock[self.headers.quantity] == '> 1000'), self.headers.quantity] = 1100
        self.__df_stock.loc[(self.__df_stock[self.headers.quantity] == 'нет'), self.headers.quantity] = pd.NA
        self.__df_stock.loc[(self.__df_stock[self.headers.rrc] == ''), self.headers.rrc] = 0
        self.__df_stock.dropna(axis=0,
                               subset=[self.headers.brand,
                                       self.headers.article,
                                       self.headers.name,
                                       self.headers.quantity,
                                       self.headers.purchase_price],
                               inplace=True)
        self.__df_stock[self.headers.rrc] = pd.to_numeric(self.__df_stock[self.headers.rrc])
        self.__df_stock[self.headers.purchase_price] = pd.to_numeric(self.__df_stock[self.headers.purchase_price])
