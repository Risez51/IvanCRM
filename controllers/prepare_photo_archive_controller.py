import os.path
import main_window
from PyQt5.QtWidgets import QTableWidgetItem

from configs import config
from file_manager.storage import Storage
from handlers.filedialog import FileDialog


class PhotoArchiveController:
    def __init__(self, ui: main_window.Ui_MainWindow):
        self.ui = ui
        self.ui.add_prepare_list_photo_push_button.clicked.connect(self.on_add_prepare_list_photo_push_button)

    def on_add_prepare_list_photo_push_button(self):
        try:
            file_location = FileDialog().get_file_name(config.PHOTO_LIST_FILE_TYPES)
            if file_location:
                dataframe = Storage().get_dataframe(os.path.abspath(file_location))
                headers = list(map(self.decode_to_correct, dataframe.columns.values.tolist()))
                headers.append('Статус')
                self.ui.articles_without_photo_table_widget.setColumnCount(len(headers))

                self.ui.articles_without_photo_table_widget.setHorizontalHeaderLabels(headers)
                for i, row in dataframe.iterrows():
                    # Добавление строки
                    self.ui.articles_without_photo_table_widget.setRowCount(
                        self.ui.articles_without_photo_table_widget.rowCount() + 1)
                    for j in range(self.ui.articles_without_photo_table_widget.columnCount() - 1):
                        if j == 1:
                            name = self.decode_to_correct(str(row[j]))
                            self.ui.articles_without_photo_table_widget.setItem(i, j, QTableWidgetItem(name))
                        else:
                            self.ui.articles_without_photo_table_widget.setItem(i, j, QTableWidgetItem(str(row[j])))
        except Exception as e:
            print(e)

    def add_data_to_table_widget(self, file_location):
        dataframe = Storage().get_dataframe(file_location)
        pass

    @staticmethod
    def decode_to_correct(string: str):
        return string.encode('latin-1').decode('cp1251')
