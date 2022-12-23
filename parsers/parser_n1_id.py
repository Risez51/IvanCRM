from parsers import parsing_parameters as pp
from parsers.result_dataframe import ResultDataFrame
from file_manager.storage import Storage
import pandas as pd


class ParserN1:
    def get_result(self, files_list: list) -> pd.DataFrame:
        df_price = self.get_price_dataframe(files_list)
        df_stock = self.get_stock_dataframe(files_list)
        df_rrc = self.get_rrc_dataframe(files_list)
        merged_dataframe = self.merge_prices(df_price, df_rrc, df_stock)
        self.normalize_dataframe(merged_dataframe)
        df_result = self.get_result_dataframe(merged_dataframe)
        df_result.drop_duplicates(subset=['Артикул'], inplace=True)
        return df_result

    @staticmethod
    def get_result_dataframe(external_dataframe) -> pd.DataFrame:
        result = ResultDataFrame()
        result.set_article(external_dataframe['Артикул'])
        result.set_name(external_dataframe['Номенклатура, Характеристика, Упаковка'].str.replace(', ,', ','))
        result.set_purchase_price((external_dataframe['Москва-Ясенево, МЕЛКООПТОВАЯ'] / pp.NDS).round(2))
        result.set_quantity(external_dataframe['Доступно'])
        result.set_selling_price((result.get_purchase_price() * pp.N1_MARGIN).round(2))
        result.get_result_dataframe().loc[(result.get_selling_price() < external_dataframe['МРЦ'] / pp.NDS),
                                          'Цена продажи, б/ндс'] = (external_dataframe['МРЦ'] / pp.NDS).round(2)
        result.set_site_name(result.get_name())
        return result.get_result_dataframe()

    @staticmethod
    def normalize_dataframe(df: pd.DataFrame):
        df.loc[(pd.to_numeric(df['Доступно']) < 1), 'Доступно'] = pd.NA
        df.loc[(df['Артикул'] == '75/4') | (df['Артикул'] == '75/10'), 'Артикул'] = pd.NA
        df[~df['Номенклатура, Характеристика, Упаковка'].str.contains('|'.join(pp.N1_NEEDFUL_BRANDS),
                                                                      na=False,
                                                                      case=False)] = pd.NA
        df.dropna(axis=0, subset=['Артикул',
                                  'Москва-Ясенево, МЕЛКООПТОВАЯ',
                                  'Доступно'], inplace=True)

        df['Москва-Ясенево, МЕЛКООПТОВАЯ'] = pd.to_numeric(df['Москва-Ясенево, МЕЛКООПТОВАЯ'])
        df['МРЦ'] = pd.to_numeric(df['МРЦ'])

    @staticmethod
    def merge_prices(df_price: pd.DataFrame, df_rrc: pd.DataFrame, df_stock: pd.DataFrame) -> pd.DataFrame:
        df_price.dropna(how='all', axis=1, inplace=True)
        df_rrc.dropna(how='all', axis=1, inplace=True)
        df_stock.dropna(how='all', axis=1, inplace=True)
        df_price.dropna(axis=0, subset=['Москва-Ясенево, МЕЛКООПТОВАЯ'], inplace=True)
        df_price = df_price.merge(df_stock, how='left', left_on='Артикул', right_on='Артикул')
        df_price = df_price.merge(df_rrc, how='left', left_on='Артикул', right_on='артикул')
        return df_price

    @staticmethod
    def get_price_dataframe(fileslist: list) -> pd.DataFrame:
        for filename in fileslist:
            if 'мелкий' in filename.lower():
                return Storage().get_dataframe(filename, start_row=2)

    @staticmethod
    def get_stock_dataframe(fileslist: list) -> pd.DataFrame:
        for filename in fileslist:
            if 'остатки' in filename.lower():
                return Storage().get_dataframe(filename, start_row=7)

    @staticmethod
    def get_rrc_dataframe(fileslist: list) -> pd.DataFrame:
        for filename in fileslist:
            if 'ррц' in filename.lower() or 'мдц' in filename.lower():
                return Storage().get_dataframe(filename, start_row=1)
