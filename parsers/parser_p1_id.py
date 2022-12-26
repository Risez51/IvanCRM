from parsers.result_dataframe import ResultDataFrame
from file_manager.storage import Storage
import pandas as pd
from configs import config


class ParserP1(ResultDataFrame):
    def __init__(self, file_path: str):
        super().__init__()
        self.__df_stock = Storage().get_dataframe(file_path)
        self.headers = config.P1_HEADERS

    def get_result(self) -> pd.DataFrame:
        self.__normalize_dataframe()
        self.__fill_frame()
        return self.get_result_dataframe()

    def __fill_frame(self):
        self.set_article(self.__df_stock[self.headers.article])
        self.set_name(self.__df_stock[self.headers.name])
        self.set_purchase_price((self.__df_stock[self.headers.purchase_price] / config.NDS).round(2))
        self.set_quantity(self.__df_stock[self.headers.quantity])
        self.set_brand(self.__df_stock[self.headers.brand])
        self.set_selling_price((self.get_purchase_price() * config.P1_MARGIN).round(2))
        self.get_result_dataframe().loc[(self.get_purchase_price() < self.__df_stock[self.headers.rrc] / config.NDS),
                                        self.get_purchase_price_column_name()] = (self.__df_stock[self.headers.rrc]
                                                                                  / config.NDS).round(2)
        self.set_site_name(self.get_name())
        self.set_multiplicity(self.__df_stock[self.headers.multiplicity])

    def __normalize_dataframe(self):
        self.__df_stock.loc[(pd.to_numeric(self.__df_stock[self.headers.quantity]) < 1), self.headers.quantity] = pd.NA
        self.__df_stock[
            ~self.__df_stock[self.headers.brand].str.contains('|'.join(config.P1_NEEDFUL_BRANDS),
                                                              na=False,
                                                              case=False)] = pd.NA
        self.__df_stock.dropna(axis=0,
                               subset=[self.headers.article,
                                       self.headers.name,
                                       self.headers.quantity,
                                       self.headers.purchase_price],
                               inplace=True)
        self.__df_stock[self.headers.purchase_price] = pd.to_numeric(self.__df_stock[self.headers.purchase_price])
        self.__df_stock[self.headers.rrc] = pd.to_numeric(self.__df_stock[self.headers.rrc])
        self.__df_stock.loc[(self.__df_stock[self.headers.quantity] > 1_000_000), self.headers.quantity] = 100_000
