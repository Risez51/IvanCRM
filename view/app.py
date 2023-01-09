from PyQt5 import QtWidgets
from controllers.pasport_protection_controller import PassportProtectionController
from controllers.parser_controller import ParserController
from controllers.parser_parameters_controller import ParsingParameterController
import main_window
import parsing_parameters


class App(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Widgets
        self.parsing_parameters_widget = parsing_parameters.ParsingParametersUi()  # parsing_parameters_widget (new form window)

        # Controllers
        # 1.Controllers main window
        self.passport_protection_controller = PassportProtectionController(self)
        self.parser_controller = ParserController(self)
        # 2.Controller Settings/Parsing_parameters widget
        self.parser_parameters_controller = ParsingParameterController(self.parsing_parameters_widget)
        # Connectors
        # Opened parsing parameters widget by click menubar/settings/parsing parameters
        self.parsing_parameters_action.triggered.connect(self.on_click_settings_parsing_parameters)

    def on_click_settings_parsing_parameters(self):
        self.parsing_parameters_widget.show()
