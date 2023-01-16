from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTreeWidget

from orders.passport_protection_order import PassportProtectionOrder


class PassportProtectionOrdersHandler:

    def __init__(self, tree_widget: QTreeWidget):
        self.__tree_widget = tree_widget
        self.__orders = []

    def new_order(self, file_location):
        order = PassportProtectionOrder(self.__tree_widget)
        order.set_values(file_location)
        self.__orders.append(order)

    def get_orders(self):
        return self.__orders

    def remove_selected_order(self):
        items = self.__tree_widget.selectedItems()
        for item in items:
            self.__tree_widget.invisibleRootItem().removeChild(item)
            for order in self.__orders:
                if item == order:
                    self.__orders.remove(order)

    @staticmethod
    def set_order_status(order: PassportProtectionOrder, color: str, text: str):
        tree_widget_item = order.get_tree_widget_item()
        color = QColor(color)
        tree_widget_item.setBackground(0, color)
        tree_widget_item.setBackground(1, color)
        tree_widget_item.setBackground(2, color)
        tree_widget_item.setText(2, text)
