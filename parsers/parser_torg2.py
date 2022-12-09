from parsers import parsing_parameters as pp
from file_manager.storage import Storage
import pandas as pd


class ParserTorg2:
    def get_result(self) -> pd.DataFrame:
        price_path = pp.LOCAL_PRICE_PATH + '/Торг2_ЧК/Предложение инструмент новый.xls'
        df_stock = Storage().get_dataframe(price_path, start_row=12)
        self.normalize_dataframe(df_stock)

        df_result = pd.DataFrame()
        df_result['Артикул'] = ''
        df_result['Наименование'] = df_stock['Наименование']
        df_result['Ед.изм'] = df_stock['Ед. изм.']
        df_result['Цена поставки, б/ндс'] = df_stock['Цена перечислением без НДС']
        df_result['Количество'] = df_stock['Количество']
        df_result['РРЦ'] = ''
        df_result['РОЦ'] = ''
        df_result['Бренд'] = ''
        df_result['Цена продажи, б/ндс'] = df_result['Цена поставки, б/ндс'] * pp.TORG2_MARGIN
        df_result['Код группы'] = ''
        df_result['Наименование для сайтов'] = df_stock['Наименование']
        df_result['Кратность'] = ''
        return df_result

    @staticmethod
    def normalize_dataframe(df: pd.DataFrame):
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