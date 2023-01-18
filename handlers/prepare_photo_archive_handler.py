from pandas import DataFrame
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from orders.passport_protection_order import PassportProtectionOrder

class PreparePhotoArchiveHandler:
    __articles_without_photo: DataFrame
    __photo_archive_dir_path: str
    __result_path: str
    __orders: list[PassportProtectionOrder]

    def __init__(self, table_widget: QTableWidget):
        self.table_widget = table_widget

    def set_table(self, dataframe: DataFrame):
        self.__articles_without_photo = dataframe
        self.__set_headers()

    def set_archive_path(self, archive_path: str):
        self.__photo_archive_dir_path = archive_path

    def set_result_path(self, result_path: str):
        self.__result_path = result_path

    def create_result_archive(self):
        pass

    def __new_orders(self):
        for i, row in self.__articles_without_photo.iterrows():
            # Добавление строки
            self.table_widget.setRowCount(self.table_widget.rowCount() + 1)
            for j in range(self.table_widget.columnCount() - 1):
                if j == 1:
                    name = self.decode_to_correct(str(row[j]))
                    self.table_widget.setItem(i, j, QTableWidgetItem(name))
                else:
                    self.table_widget.setItem(i, j, QTableWidgetItem(str(row[j])))

    def __set_headers(self):
        headers = list(map(self.decode_to_correct, self.__articles_without_photo.columns.values.tolist()))
        headers.append('Статус')
        self.table_widget.setColumnCount(len(headers))
        self.table_widget.setHorizontalHeaderLabels(headers)

    @staticmethod
    def decode_to_correct(string: str):
        return string.encode('latin-1').decode('cp1251')