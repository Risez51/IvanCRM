from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore
import os


class Speaker(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    @staticmethod
    def show_message_on_result_ready(result_path: str):
        msg_answer = QMessageBox.question(None, 'Обработка завершена',
                                          'Открыть папку с файлами?',
                                          QMessageBox.Yes, QMessageBox.No)
        if msg_answer == QMessageBox.Yes:
            os.system(r'explorer.exe ' + f'{result_path}')

    @staticmethod
    def show_message_on_parsing_error(msg: str = ''):
        QMessageBox.critical(None, 'Ошибка',
                             msg,
                             QMessageBox.Ok)

    @staticmethod
    def show_message(title: str, message: str):
        msg = QMessageBox()
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec_()
