import main_window
import os
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QTreeWidgetItem
from PyQt5 import QtCore
from PyQt5.QtGui import QColor

from controllers import worker


class PassportProtectionController:
    def __init__(self, ui: main_window.Ui_MainWindow):
        self.ui = ui
        # Thread passport_protection
        self.thread = QtCore.QThread()
        self.my_worker = worker.Worker()
        self.my_worker.moveToThread(self.thread)
        self.my_worker.file_protection_started.connect(self.on_file_protect_started)
        self.my_worker.file_protection_finished.connect(self.on_file_protect_finished)
        self.my_worker.passport_protection_completed.connect(self.show_message_on_result_ready)
        self.thread.started.connect(self.my_worker.run_passport_protection)

        # GUI elements connectors
        ui.add_passport_files_push_button.clicked.connect(self.on_add_passport_files_push_button)
        ui.delete_selected_passport_file_push_button.clicked.connect(self.on_delete_selected_passport_file_push_button)
        ui.start_passport_protection_push_button.clicked.connect(self.on_start_passport_protection_push_button)
        ui.set_result_path_push_button.clicked.connect(self.on_set_result_path_push_button)
        ui.test_push_button.clicked.connect(self.on_test_push_button)

    def on_add_passport_files_push_button(self):
        opened_files = QFileDialog.getOpenFileNames(None, 'Выберите паспорта .doc .pdf', '', '*.doc *.pdf')
        for file_item in opened_files[0]:
            tree_item = QTreeWidgetItem(self.ui.passport_tree_widget)
            dir_path = os.path.abspath(os.path.dirname(file_item))
            file_name = os.path.basename(file_item)
            self.set_text_to_tree_item_dir_path_column(tree_item, dir_path)
            self.set_text_to_tree_item_file_name_column(tree_item, file_name)
            self.set_text_to_tree_item_status_column(tree_item, 'Добавлен')

    def on_delete_selected_passport_file_push_button(self):
        for item in self.ui.passport_tree_widget.selectedItems():
            self.ui.passport_tree_widget.invisibleRootItem().removeChild(item)

    def on_start_passport_protection_push_button(self):
        if self.ui.result_path_line_edit.text() != '':
            output_dir = self.ui.result_path_line_edit.text()
            files_dict = self.get_tree_items()
            if files_dict:
                self.my_worker.set_params(files_dict, output_dir)
                self.thread.start()
            else:
                self.show_message('Ошибка', 'Добавьте файлы для обработки')
        else:
            self.show_message('Ошибка', 'Введите путь для итоговых файлов')

    def on_test_push_button(self):
        pass

    # Set status in process..
    def on_file_protect_started(self, item_index: int, message: str):
        self.set_tree_item_status(item_index, message, '#FFFF00')

    def on_file_protect_finished(self, item_index: int, message: str):
        self.set_tree_item_status(item_index, message, '#33FF33')

    def on_set_result_path_push_button(self):
        output_dir_path = os.path.abspath(QFileDialog.getExistingDirectory(None, 'Выберите папку...'))
        self.ui.result_path_line_edit.setText(output_dir_path)

    def on_file_protection_is_ready(self, message: str):
        self.ui.statusbar.showMessage(message)

    def get_tree_items(self) -> dict:
        root = self.ui.passport_tree_widget.invisibleRootItem()
        files_dict = {}
        for i in range(root.childCount()):
            item = root.child(i)
            dir_path = item.text(0)
            file_name = item.text(1)
            files_dict[i] = dir_path + '\\' + file_name
        return files_dict

    def set_tree_item_status(self, item_index: int, message: str, color_hex: str):
        color = QColor(color_hex)
        self.ui.passport_tree_widget.invisibleRootItem().child(item_index).setBackground(0, color)
        self.ui.passport_tree_widget.invisibleRootItem().child(item_index).setBackground(1, color)
        self.ui.passport_tree_widget.invisibleRootItem().child(item_index).setBackground(2, color)
        self.ui.passport_tree_widget.invisibleRootItem().child(item_index).setText(2, message)

    def show_message_on_result_ready(self):
        msg_answer = QMessageBox.question(None, 'Обработка завершена',
                                          'Открыть папку с файлами?',
                                          QMessageBox.Yes, QMessageBox.No)
        if msg_answer == QMessageBox.Yes:
            result_path = self.ui.result_path_line_edit.text() + "\\Паспорта с защитой"
            os.system(r'explorer.exe ' + f'{result_path}')

    @staticmethod
    def show_message(title: str, message: str):
        msg = QMessageBox()
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec_()

    @staticmethod
    def set_text_to_tree_item_dir_path_column(item: QTreeWidgetItem, text: str):
        item.setText(0, text)

    @staticmethod
    def set_text_to_tree_item_file_name_column(item: QTreeWidgetItem, text: str):
        item.setText(1, text)

    @staticmethod
    def set_text_to_tree_item_status_column(item: QTreeWidgetItem, text: str):
        item.setText(2, text)
