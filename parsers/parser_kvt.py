from file_manager.storage import Storage
import pandas as pd
from parsers.result_dataframe import ResultDataFrame
from configs import config


class ParserKVT(ResultDataFrame):
    def __init__(self, file_path: str):
        super().__init__()
        if file_path == '':
            file_path = config.KVT_LINK
        self.__df_stock = Storage().get_dataframe(file_path, start_row=1)
        self.headers = config.KVT_HEADERS

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
        self.set_selling_price(self.get_purchase_price())
        self.set_site_name(self.get_name())

    def normalize_dataframe(self):
        self.__df_stock.dropna(axis=0,
                               subset=[self.headers.article,
                                       self.headers.name,
                                       self.headers.quantity,
                                       self.headers.purchase_price],
                               inplace=True)
        self.__df_stock[self.headers.quantity] = pd.to_numeric(self.__df_stock[self.headers.quantity])
        self.__df_stock.loc[(self.__df_stock[self.headers.quantity] > 1_000_000), self.headers.quantity] = 100_000
