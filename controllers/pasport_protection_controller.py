import main_window
import os
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QTreeWidgetItem
from actions.passport_protection import PassportProtection
from PyQt5 import QtCore
from controllers import worker


class PassportProtectionController:
    def __init__(self, ui: main_window.Ui_MainWindow):
        self.ui = ui
        self.thread = QtCore.QThread()
        self.my_worker = worker.Worker()
        self.my_worker.moveToThread(self.thread)
        self.my_worker.index_changed.connect(self.on_index_changed)
        self.thread.started.connect(self.my_worker.run)
        self.thread.start()

        ui.add_passport_files_push_button.clicked.connect(self.on_add_passport_files_push_button)
        ui.delete_selected_passport_file_push_button.clicked.connect(self.on_delete_selected_passport_file_push_button)
        ui.start_passport_protection_push_button.clicked.connect(self.on_start_passport_protection_push_button)
        ui.set_result_path_push_button.clicked.connect(self.on_set_result_path_push_button)

    def on_add_passport_files_push_button(self):
        opened_files = QFileDialog.getOpenFileNames(None, 'Выберите паспорта .doc .pdf', '', '*.doc *.pdf')
        for file_item in opened_files[0]:
            tree_item = QTreeWidgetItem(self.ui.passport_tree_widget)
            tree_item.setText(0, os.path.dirname(file_item))
            tree_item.setText(1, os.path.basename(file_item))
            tree_item.setText(2, 'Добавлен')

    def on_delete_selected_passport_file_push_button(self):
        for item in self.ui.passport_tree_widget.selectedItems():
            self.ui.passport_tree_widget.invisibleRootItem().removeChild(item)

    def on_start_passport_protection_push_button(self):
        if self.ui.result_path_line_edit.text() != '':
            root = self.ui.passport_tree_widget.invisibleRootItem()
            child_count = root.childCount()
            for i in range(child_count):
                item = root.child(i)
                dir_path = item.text(0)
                file_name = item.text(1)
                self.ui.statusbar.showMessage(f'Обработка {file_name}')
                output_dir = self.ui.result_path_line_edit.text()
                PassportProtection(os.path.abspath(dir_path), output_dir).start_one(file_name)
                item.setText(2, 'Готово')
            self.show_message_on_result_ready()
            self.ui.statusbar.showMessage(f'')

    def on_set_result_path_push_button(self):
        output_dir_path = os.path.abspath(QFileDialog.getExistingDirectory(None, 'Выберите папку...'))
        self.ui.result_path_line_edit.setText(output_dir_path)

    def show_message_on_result_ready(self):
        msg_answer = QMessageBox.question(None, 'Обработка завершена',
                                          'Открыть папку с файлами?',
                                          QMessageBox.Yes, QMessageBox.No)
        if msg_answer == QMessageBox.Yes:
            result_path = self.ui.result_path_line_edit.text() + "\\Паспорта с защитой"
            os.system(r'explorer.exe ' + f'{result_path}')

    #@QtCore.pyqtSlot(int)
    def on_index_changed(self, i):
        self.ui.result_path_line_edit.setText(str(i))
