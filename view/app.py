import main_window

from PyQt5 import QtWidgets
from controllers.pasport_protection_controller import PassportProtectionController


class App(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.passport_protection_controller = PassportProtectionController(self)












