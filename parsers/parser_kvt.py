from parsers import parsing_parameters as pp
from file_manager.storage import Storage
import pandas as pd


class ParserKVT:

    def get_result(self) -> pd.DataFrame:
        df_stock = Storage().get_dataframe(pp.KVT_LINK, start_row=1)
        self.normalize_dataframe(df_stock)

        df_result = pd.DataFrame()
        df_result['Артикул'] = df_stock['код товара']
        df_result['Наименование'] = df_stock['Наименование']
        df_result['Ед.изм'] = df_stock['ед.изм.']
        df_result['Цена поставки, б/ндс'] = (df_stock['РРЦ'] / pp.NDS).round(2)
        df_result['Количество'] = df_stock['на складе (кол-во)']
        df_result['РРЦ'] = ''
        df_result['РОЦ'] = ''
        df_result['Бренд'] = ''
        df_result['Цена продажи, б/ндс'] = df_result['Цена поставки, б/ндс'].round(2)
        df_result['Код группы'] = ''
        df_result['Наименование для сайтов'] = df_stock['Наименование']
        df_result['Кратность'] = ''
        return df_result

    @staticmethod
    def normalize_dataframe(df: pd.DataFrame):
        df.dropna(axis=0,
                  subset=['код товара',
                          'Наименование',
                          'на складе (кол-во)',
                          'РРЦ'],
                  inplace=True)
        df['на складе (кол-во)'] = pd.to_numeric(df['на складе (кол-во)'])
        df.loc[(df['на складе (кол-во)'] > 1_000_000), 'на складе (кол-во)'] = 100_000
