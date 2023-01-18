import os
import main_window
from PyQt5.QtWidgets import QTableWidgetItem

from configs import config
from file_manager.storage import Storage
from handlers.filedialog import FileDialog
from actions.prepare_photo_archive import PreparePhotoArchive


class PhotoArchiveController:
    def __init__(self, ui: main_window.Ui_MainWindow):
        self.ui = ui
        self.ui.add_prepare_list_photo_push_button.clicked.connect(self.on_add_prepare_list_photo_push_button)
        self.ui.add_photo_archive_path_push_button.clicked.connect(self.on_add_photo_archive_push_button)
        self.ui.add_result_path_archive_push_button.clicked.connect(self.on_add_result_path_archive_push_button)
        self.ui.start_prepare_result_archive_push_button.clicked.connect(
            self.on_start_prepare_result_archive_push_button)

    def on_add_prepare_list_photo_push_button(self):
        try:
            file_location = FileDialog().get_file_name(config.PHOTO_LIST_FILE_TYPES)
            if file_location:
                dataframe = Storage().get_dataframe(file_location)
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

    def on_add_photo_archive_push_button(self):
        dir_path = FileDialog().get_dir_path()
        self.ui.photo_archive_path_line_edit.setText(dir_path)

    def on_add_result_path_archive_push_button(self):
        dir_path = FileDialog().get_dir_path()
        self.ui.result_path_archive_line_edit.setText(dir_path)

    def on_start_prepare_result_archive_push_button(self):
        rows_count = self.ui.articles_without_photo_table_widget.rowCount()
        status_column_index = self.ui.articles_without_photo_table_widget.columnCount()-1
        result_path = self.ui.result_path_archive_line_edit.text()
        archive_path = self.ui.photo_archive_path_line_edit.text()
        for i in range(rows_count):
            article = self.ui.articles_without_photo_table_widget.item(i, 0).text()
            folder_with_photo_name = archive_path + '\\' + article
            if os.path.exists(folder_with_photo_name):
                print(folder_with_photo_name)
                PreparePhotoArchive(archive_path, result_path).start_one(article)
                self.ui.articles_without_photo_table_widget.setItem(i, status_column_index, QTableWidgetItem('Готово'))
            else:
                self.ui.articles_without_photo_table_widget.setItem(i, status_column_index, QTableWidgetItem('Не найден'))
            print(article)

    @staticmethod
    def decode_to_correct(string: str):
        return string.encode('latin-1').decode('cp1251')
