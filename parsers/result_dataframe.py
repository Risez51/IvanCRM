import pandas as pd
from configs import config


class ResultDataFrame:
    def __init__(self):
        self.__df = pd.DataFrame()
        self.__df['Артикул'] = ''
        self.__df['Наименование'] = ''
        self.__df['Ед.изм'] = ''
        self.__df['Цена поставки, б/ндс'] = ''
        self.__df['Количество'] = ''
        self.__df['РРЦ'] = ''
        self.__df['РОЦ'] = ''
        self.__df['Бренд'] = ''
        self.__df['Цена продажи, б/ндс'] = ''
        self.__df['Код группы'] = ''
        self.__df['Наименование для сайтов'] = ''
        self.__df['Кратность'] = ''

    def get_result_dataframe(self):
        return self.__df

    def set_article(self, column):
        self.__df['Артикул'] = column

    def get_article(self):
        return self.__df['Артикул']

    def set_name(self, column):
        self.__df['Наименование'] = column

    def get_name(self):
        return self.__df['Наименование']

    def set_unit(self, column):
        self.__df['Ед.изм'] = column

    def get_unit(self):
        return self.__df['Ед.изм']

    def set_purchase_price(self, column):
        self.__df['Цена поставки, б/ндс'] = column

    def get_purchase_price(self):
        return self.__df['Цена поставки, б/ндс']

    def set_quantity(self, column):
        self.__df['Количество'] = column

    def get_quantity(self, column):
        return self.__df['Количество']

    def set_brand(self, column):
        self.__df['Бренд'] = column

    def get_brand(self):
        return self.__df['Бренд']

    def set_selling_price(self, column):
        self.__df['Цена продажи, б/ндс'] = column

    def get_selling_price(self):
        return self.__df['Цена продажи, б/ндс']

    def set_site_name(self, column):
        self.__df['Наименование для сайтов'] = column

    def get_site_name(self):
        return self.__df['Наименование для сайтов']

    def set_multiplicity(self, column):
        self.__df['Кратность'] = column

    def get_multiplicity(self):
        return self.__df['Кратность']

    @staticmethod
    def get_purchase_price_column_name() -> str:
        return 'Цена поставки, б/ндс'
