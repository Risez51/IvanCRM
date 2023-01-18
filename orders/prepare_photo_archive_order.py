from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from pandas import Series


class PreparePhotoArchiveOrder:
    __article: str
    __name: str

    def __init__(self, table_widget: QTableWidget):
        self.__table_widget = table_widget
        self.__item = QTableWidgetItem(table_widget)

    def new_order(self, row_index: int, row: Series):
        for j in range(self.__table_widget.columnCount() - 1):
            if j == 1:
                name = self.decode_to_correct(str(row[j]))
                self.__table_widget.setItem(row_index, j, QTableWidgetItem(name))
            else:
                self.__table_widget.setItem(row_index, j, QTableWidgetItem(str(row[j])))

    def get_article(self):
        return self.__article

    def get_name(self):
        return self.__name

    def get_table_widget_item(self):
        return self.__item

    @staticmethod
    def decode_to_correct(string: str):
        return string.encode('latin-1').decode('cp1251')
