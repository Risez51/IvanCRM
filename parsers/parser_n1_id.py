from parsers.result_dataframe import ResultDataFrame
from file_manager.storage import Storage
import pandas as pd
from configs import config


class ParserN1(ResultDataFrame):
    def __init__(self, files: list[str]):
        super().__init__()
        self.df_price = self.get_price_dataframe(files)
        self.df_stock = self.get_stock_dataframe(files)
        self.df_rrc = self.get_rrc_dataframe(files)
        self.headers = config.N1_HEADERS

    def get_result(self) -> pd.DataFrame:
        self.merge_prices()
        self.normalize_dataframe()
        self.__fill_dataframe()
        self.get_result_dataframe().drop_duplicates(subset=[self.headers.article], inplace=True)
        return self.get_result_dataframe()

    def __fill_dataframe(self):
        self.set_article(self.df_price[self.headers.article])
        self.set_name(self.df_price[self.headers.name].str.replace(', ,', ','))
        self.set_purchase_price((self.df_price[self.headers.purchase_price] / config.NDS).round(2))
        self.set_quantity(self.df_price[self.headers.quantity])
        self.set_selling_price((self.get_purchase_price() * config.N1_MARGIN).round(2))
        self.get_result_dataframe().loc[(self.get_selling_price() < self.df_price[self.headers.rrc] / config.NDS),
                                        self.get_purchase_price_column_name()] = (self.df_price[self.headers.rrc] /
                                                                                  config.NDS).round(2)
        self.set_site_name(self.get_name())

    def normalize_dataframe(self):
        self.df_price.loc[(pd.to_numeric(self.df_price[self.headers.quantity]) < 1), self.headers.quantity] = pd.NA
        self.df_price.loc[
            (self.df_price[self.headers.article] == '75/4') | (self.df_price[self.headers.article] == '75/10'),
            self.headers.article] = pd.NA
        self.df_price[
            ~self.df_price[self.headers.name].str.contains('|'.join(config.N1_NEEDFUL_BRANDS),
                                                           na=False,
                                                           case=False)] = pd.NA
        self.df_price.dropna(axis=0, subset=[self.headers.article,
                                             self.headers.purchase_price,
                                             self.headers.quantity], inplace=True)

        self.df_price[self.headers.purchase_price] = pd.to_numeric(self.df_price[self.headers.purchase_price])
        self.df_price[self.headers.rrc] = pd.to_numeric(self.df_price[self.headers.rrc])

    def merge_prices(self):
        self.df_price.dropna(how='all', axis=1, inplace=True)
        self.df_rrc.dropna(how='all', axis=1, inplace=True)
        self.df_stock.dropna(how='all', axis=1, inplace=True)
        self.df_price.dropna(axis=0, subset=[self.headers.purchase_price], inplace=True)
        self.df_price = self.df_price.merge(self.df_stock, how='left', left_on='Артикул', right_on='Артикул')
        self.df_price = self.df_price.merge(self.df_rrc, how='left', left_on='Артикул', right_on='артикул')

    @staticmethod
    def get_price_dataframe(files_list: list[str]) -> pd.DataFrame:
        for filename in files_list:
            if 'мелкий' in filename.lower():
                return Storage().get_dataframe(filename, start_row=2)

    @staticmethod
    def get_stock_dataframe(files_list: list[str]) -> pd.DataFrame:
        for filename in files_list:
            if 'остатки' in filename.lower():
                return Storage().get_dataframe(filename, start_row=7)

    @staticmethod
    def get_rrc_dataframe(files_list: list[str]) -> pd.DataFrame:
        for filename in files_list:
            if 'ррц' in filename.lower() or 'мдц' in filename.lower():
                return Storage().get_dataframe(filename, start_row=1)
