from PyQt5 import QtWidgets
from controllers.pasport_protection_controller import PassportProtectionController
from controllers.parser_controller import ParserController
from controllers.parser_parameters_controller import ParsingParameterController
from controllers.prepare_photo_archive_controller import PhotoArchiveController
import main_window
import parsing_parameters


class App(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Widgets
        # parsing_parameters_widget (new form window)
        self.parsing_parameters_widget = parsing_parameters.ParsingParametersUi()
        # Controllers
        # 1. Controllers main window
        self.passport_protection_controller = PassportProtectionController(self)
        # 2. Controller parsing window
        self.parser_controller = ParserController(self)
        # 3. Controller Settings/Parsing_parameters widget
        self.parser_parameters_controller = ParsingParameterController(self.parsing_parameters_widget)
        # 4. Controller prepare photo archive
        self.prepare_photo_archive_controller = PhotoArchiveController(self)
        # Connectors
        # Opened parsing parameters widget by click menu_bar/settings/parsing_parameters
        self.parsing_parameters_action.triggered.connect(self.on_click_settings_parsing_parameters)

    def on_click_settings_parsing_parameters(self):
        self.parsing_parameters_widget.show()
