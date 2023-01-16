from parsers.result_dataframe import ResultDataFrame
from file_manager.storage import Storage
import pandas as pd
from configs import config


class ParserTorg2(ResultDataFrame):
    def __init__(self, files: list[str]):
        super().__init__()
        self.__df_stock = Storage().get_dataframe(files[0], start_row=12)

    def get_result(self) -> pd.DataFrame:
        self.__normalize_dataframe()
        self.__fill_dataframe()
        return self.get_result_dataframe()

    def __fill_dataframe(self):
        self.set_name(self.__df_stock[config.TORG2_HEADERS.name])
        self.set_unit(self.__df_stock[config.TORG2_HEADERS.unit])
        self.set_purchase_price(self.__df_stock[config.TORG2_HEADERS.purchase_price])
        self.set_quantity(self.__df_stock[config.TORG2_HEADERS.quantity])
        self.set_selling_price(self.get_purchase_price() * config.TORG2_MARGIN)
        self.set_site_name(self.get_name())

    def __normalize_dataframe(self):
        self.__df_stock.loc[(self.__df_stock[config.TORG2_HEADERS.purchase_price] == 'договор.'),
                            config.TORG2_HEADERS.purchase_price] = pd.NA
        self.__df_stock[
            self.__df_stock[config.TORG2_HEADERS.get_name()].str.contains('|'.join(config.TORG2_EXCEPTIONS_BRANDS),
                                                                          na=False,
                                                                          case=False)
        ] = pd.NA
        self.__df_stock.dropna(axis=0,
                               subset=[config.TORG2_HEADERS.name,
                                       config.TORG2_HEADERS.quantity,
                                       config.TORG2_HEADERS.purchase_price],
                               inplace=True)
        self.__df_stock[config.TORG2_HEADERS.quantity] = pd.to_numeric(self.__df_stock[config.TORG2_HEADERS.quantity])
        self.__df_stock.loc[(self.__df_stock[config.TORG2_HEADERS.quantity] > 1_000_000),
                            config.TORG2_HEADERS.quantity] = 100_000
