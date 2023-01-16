from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
from os import path

from configs import config


class PassportProtectionOrder:
    def __init__(self, tree_widget: QTreeWidget):
        self.__tree_widget = tree_widget
        self.__tree_widget_item = QTreeWidgetItem(tree_widget)
        self.__file_location = ''

    def __eq__(self, other):
        return self.__tree_widget_item == other

    def set_values(self, file_location: str):
        dir_path = path.abspath(path.dirname(file_location))
        file_name = path.basename(file_location)
        self.__file_location = file_location
        self.__tree_widget_item.setText(0, dir_path)
        self.__tree_widget_item.setText(1, file_name)
        self.__tree_widget_item.setText(2, config.STATUS_ADDED)

    def get_tree_widget_item(self):
        return self.__tree_widget_item

    def get_file_dir(self):
        return path.dirname(self.__file_location)

    def get_file_name(self):
        return path.basename(self.__file_location)

    def get_file_location(self):
        return self.__file_location
