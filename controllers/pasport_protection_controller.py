import main_window
from PyQt5 import QtCore
from workers.passport_protection_worker import PassportProtectionWorker
from configs import config
from handlers.filedialog import FileDialog
from handlers.speaker import Speaker
from handlers.passport_protection_orders_handler import PassportProtectionOrdersHandler
from orders.passport_protection_order import PassportProtectionOrder


class PassportProtectionController:
    def __init__(self, ui: main_window.Ui_MainWindow):
        self.ui = ui
        # Thread passport_protection
        self.thread = QtCore.QThread()
        self.worker = PassportProtectionWorker()
        self.worker.moveToThread(self.thread)
        self.worker.passport_protection_started.connect(self.on_passport_protection_started)
        self.worker.passport_protection_finished.connect(self.on_passport_protection_finished)
        self.worker.passport_protection_completed.connect(self.on_passports_protection_completed)
        self.thread.started.connect(self.worker.run)
        # GUI element connectors
        ui.add_passport_files_push_button.clicked.connect(self.on_add_passport_files_push_button)
        ui.delete_selected_passport_file_push_button.clicked.connect(self.on_delete_selected_passport_file_push_button)
        ui.start_passport_protection_push_button.clicked.connect(self.on_start_passport_protection_push_button)
        ui.set_result_path_push_button.clicked.connect(self.on_set_result_path_push_button)
        # Orders handler
        self.__orders_handler = PassportProtectionOrdersHandler(self.ui.passport_tree_widget)

    # Added files (tree widget items) in tree widget
    def on_add_passport_files_push_button(self):
        opened_files: list[str] = FileDialog().get_file_names(config.PASSPORT_FILE_TYPES)
        if opened_files:
            for file_location in opened_files:
                self.__orders_handler.new_order(file_location)

    # Delete row from tree widget
    def on_delete_selected_passport_file_push_button(self):
        self.__orders_handler.remove_selected_order()

    # Start passport protection
    def on_start_passport_protection_push_button(self):
        if self.ui.result_path_line_edit.text() != '':
            output_dir = self.ui.result_path_line_edit.text()
            orders = self.__orders_handler.get_orders()
            if orders:
                self.worker.set_params(orders, output_dir)
                self.thread.start()
            else:
                Speaker().show_message('Недостаточно данных', 'Добавьте файлы для обработки')
        else:
            Speaker().show_message('Недостаточно данных', 'Введите путь для итоговых файлов')

    # Заполнеят result line edit -> result path directory
    def on_set_result_path_push_button(self):
        output_dir_path = FileDialog().get_dir_path()
        if output_dir_path:
            self.ui.result_path_line_edit.setText(output_dir_path)

    # SIGNALS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Set status 'process'
    def on_passport_protection_started(self, order: PassportProtectionOrder):
        self.__orders_handler.set_order_status(order, config.STATUS_PROCESSING_COLOR, config.STATUS_PROCESSING)

    # Set status 'finished'
    def on_passport_protection_finished(self, order: PassportProtectionOrder):
        self.__orders_handler.set_order_status(order, config.STATUS_READY_COLOR, config.STATUS_READY)

    # on received protection for all passport files
    def on_passports_protection_completed(self):
        self.thread.quit()
        result_path = self.ui.result_path_line_edit.text() + "\\Паспорта с защитой"
        Speaker().show_message_on_result_ready(result_path)
    # SIGNALS---------------------------------------------------------
