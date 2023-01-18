from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QComboBox
from os import path
from multipledispatch import dispatch
from configs import config


class ManualParserOrder:

    def __init__(self, tree_widget: QTreeWidget):
        self.__tree_widget = tree_widget
        self.__tree_widget_item = QTreeWidgetItem(tree_widget)
        self.__files = []

    def __eq__(self, other):
        return self.__tree_widget_item == other

    # Создает TreeWidgetItem для 1-го файла
    @dispatch(str)
    def set_values(self, file_location: str):
        self.__tree_widget_item.setText(0, path.dirname(file_location))
        self.__tree_widget_item.setText(1, path.basename(file_location))
        self.__add_combobox_to_manual_parser_tree_widget_item(2, self.__tree_widget_item)
        self.__files.append(file_location)

    # Создает TreeWidgetItem из нескольких файлов
    @dispatch(list)
    def set_values(self, file_locations: list[str]):
        self.__tree_widget_item.setText(0, path.dirname(file_locations[0]))
        file_names = self.__create_multiple_file_names(file_locations)
        self.__files = file_locations
        self.__tree_widget_item.setText(1, file_names)
        self.__add_combobox_to_manual_parser_tree_widget_item(2, self.__tree_widget_item)

    def get_tree_widget_item(self):
        return self.__tree_widget_item

    # Возвращает список файлов [расположение\имя_файла,...]
    def get_files(self) -> list[str]:
        return self.__files

    # Возвращает имя поставщика (Текущий текст в combobox)
    def get_supplier_name(self):
        self.__convert_combobox_to_text(self.__tree_widget_item, 2)
        return self.__tree_widget_item.text(2)

    # Создает комбобокс со списком поставщиков в TreeWidgetItem
    def __add_combobox_to_manual_parser_tree_widget_item(self, column: int, item: QTreeWidgetItem):
        combobox = QComboBox()
        combobox.addItems(config.SUPPLIERS)
        self.__tree_widget.setItemWidget(item, column, combobox)

    # Конвертирует combobox в текстовое поле
    def __convert_combobox_to_text(self, item: QTreeWidgetItem, column: int):
        if isinstance(self.__tree_widget.itemWidget(item, column), QComboBox):
            combobox_value = self.__tree_widget.itemWidget(item, column).currentText()
            self.__tree_widget.removeItemWidget(item, column)
            item.setText(column, combobox_value)

    @staticmethod
    def __create_multiple_file_names(files: list) -> str:
        return ';'.join(list(map(path.basename, files)))
