from parsers import parsing_parameters as pp
from file_manager.storage import Storage
import pandas as pd


class ParserYu1:
    def get_result(self) -> pd.DataFrame:
        price_path = pp.LOCAL_PRICE_PATH + '/Ю1_ИД/Прайс_1.xlsx'
        df_stock = Storage().get_dataframe(price_path)
        self.normalize_dataframe(df_stock)

        df_result = pd.DataFrame()
        df_result['Артикул'] = df_stock['Модификация']
        df_result['Наименование'] = df_stock['Название']
        df_result['Ед.изм'] = df_stock['Ед.изм.']
        df_result['Цена поставки, б/ндс'] = (df_stock['ЦЕНА клиента'] / pp.NDS).round(2)
        df_result['Количество'] = df_stock['Наличие']
        df_result['РРЦ'] = ''
        df_result['РОЦ'] = ''
        df_result['Бренд'] = df_stock['Торговая марка']
        df_result['Цена продажи, б/ндс'] = (df_stock['ЦЕНА клиента'] / pp.NDS * pp.YU1_MARGIN).round(2)
        df_result.loc[(pd.to_numeric(df_stock['РРЦ']) > 0), 'Цена продажи, б/ндс'] = (df_stock['РРЦ'] / pp.NDS).round(2)
        df_result['Код группы'] = ''
        df_result['Наименование для сайтов'] = df_stock['Название']
        df_result['Кратность'] = df_stock['Min кол-во отгрузки']
        return df_result

    @staticmethod
    def normalize_dataframe(df: pd.DataFrame):
        df[~df['Торговая марка'].str.contains('|'.join(pp.YU1_NEEDFUL_BRANDS), na=False, case=False)] = pd.NA
        df.loc[(df['Наличие'] == '< 10'), 'Наличие'] = 9
        df.loc[(df['Наличие'] == '> 10'), 'Наличие'] = 15
        df.loc[(df['Наличие'] == '> 50'), 'Наличие'] = 60
        df.loc[(df['Наличие'] == '> 100'), 'Наличие'] = 150
        df.loc[(df['Наличие'] == '> 500'), 'Наличие'] = 600
        df.loc[(df['Наличие'] == '> 1000'), 'Наличие'] = 1100
        df.loc[(df['Наличие'] == 'нет'), 'Наличие'] = pd.NA
        df.loc[(df['РРЦ'] == ''), 'РРЦ'] = 0
        df.dropna(axis=0,
                  subset=['Торговая марка',
                          'Модификация',
                          'Название',
                          'Наличие',
                          'ЦЕНА клиента'],
                  inplace=True)
        df['РРЦ'] = pd.to_numeric(df['РРЦ'])
        df['ЦЕНА клиента'] = pd.to_numeric(df['ЦЕНА клиента'])

