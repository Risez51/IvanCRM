import os
import pathlib
import sys  # sys нужен для передачи argv в QApplication
import main_window
from PyQt5 import QtWidgets
from actions.passport_protection import PassportProtection


class App(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__listWidgetItems = []
        self.__files_dir = ''
        self.addFilesPushButton.clicked.connect(self.on_push_add_files_button)
        self.deletePushButton.clicked.connect(self.on_push_delete_button)
        self.startPushButton.clicked.connect(self.on_start_push_button)

    def on_push_add_files_button(self):
        opened_files = QtWidgets.QFileDialog.getOpenFileNames(self, 'Выберите паспорта .doc .pdf', '', '*.doc *.pdf')
        self.__listWidgetItems = opened_files[0]
        self.listWidget.addItems([os.path.basename(file) for file in opened_files[0] if opened_files[0]])

    def on_push_delete_button(self):
        items = self.listWidget.selectedItems()
        print(items)
        for item in items:
            print(item)
            self.listWidget.takeItem(self.listWidget.row(item))

    def on_start_push_button(self):
        dir_path = os.path.dirname(self.__listWidgetItems[0])
        file_name = os.path.basename(self.__listWidgetItems[0])
        print(dir_path)
        print(file_name)
        PassportProtection(os.path.abspath(dir_path)).start_one(file_name)
