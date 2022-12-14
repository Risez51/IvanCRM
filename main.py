import sys
from PyQt5 import QtWidgets
from view.app import App
from view.user_console_interaction import UserConsoleInteraction


def main():
    run_gui()
    # UserConsoleInteraction().start()


def run_gui():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
