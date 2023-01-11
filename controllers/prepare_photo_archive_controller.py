import main_window
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem


class PhotoArchiveController:
    def __init__(self, ui: main_window.Ui_MainWindow):
        self.ui = ui
        self.ui.add_prepare_list_photo_push_button.clicked.connect(self.on_add_prepare_list_photo_push_button)

    def on_add_prepare_list_photo_push_button(self):
        try:
            itm = QTableWidgetItem('text')
            self.ui.articles_without_photo_table_widget.setRowCount(1)
            self.ui.articles_without_photo_table_widget.setColumnCount(3)
            self.ui.articles_without_photo_table_widget.setItem(0,0, itm)
        except Exception as e:
            print(e)
        #opened_file = QFileDialog.getOpenFileNames(None, 'Выберите файлы', '', '.xls .xlsx .csv')


    def add_data_to_table_widget(self, data):
        pass