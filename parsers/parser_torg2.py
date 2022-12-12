from parsers import parsing_parameters as pp
from parsers.result_dataframe import ResultDataFrame
from file_manager.storage import Storage
import pandas as pd


class ParserTorg2(ResultDataFrame):
    def __init__(self):
        super().__init__()
        path_with_prices = pp.LOCAL_PRICE_PATH + '/Торг2_ЧК/'
        files_list = Storage().get_filenames(pp.LOCAL_PRICE_PATH + '/Торг2_ЧК/')
        self.__df_stock = Storage().get_dataframe(path_with_prices + '/' + files_list[0], start_row=12)

    def get_result(self) -> pd.DataFrame:
        self.__normalize_dataframe(self.__df_stock)
        self.__fill_dataframe(self.__df_stock)
        return self.get_result_dataframe()

    def __fill_dataframe(self, external_dataframe):
        self.set_name(external_dataframe['Наименование'])
        self.set_unit(external_dataframe['Ед. изм.'])
        self.set_purchase_price(external_dataframe['Цена перечислением без НДС'])
        self.set_quantity(external_dataframe['Количество'])
        self.set_selling_price(self.get_purchase_price() * pp.TORG2_MARGIN)
        self.set_site_name(external_dataframe['Наименование'])

    @staticmethod
    def __normalize_dataframe(df: pd.DataFrame):
        df.loc[(df['Цена перечислением без НДС'] == 'договор.'), 'Цена перечислением без НДС'] = pd.NA
        df[df['Наименование'].str.contains('|'.join(pp.TORG2_EXCEPTIONS_BRANDS), na=False, case=False)] = pd.NA
        df.dropna(axis=0,
                  subset=['артикул',
                          'Наименование',
                          'Количество',
                          'Цена перечислением без НДС'],
                  inplace=True)
        df['Количество'] = pd.to_numeric(df['Количество'])
        df.loc[(df['Количество'] > 1_000_000), 'Количество'] = 100_000
