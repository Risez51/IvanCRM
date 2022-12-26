import sys
from PyQt5 import QtWidgets
from view.app import App


def main():
    run_gui()


def run_gui():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
