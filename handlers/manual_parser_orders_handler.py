from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTreeWidget
from orders.manual_parser_order import ManualParserOrder


class ManualParserOrdersHandler:
    def __init__(self, tree_widget: QTreeWidget):
        self.__tree_widget = tree_widget
        self.__orders = []

    # Создает новую заявку
    def new_order(self, file_location):
        order = ManualParserOrder(self.__tree_widget)
        order.set_values(file_location)
        self.__orders.append(order)

    # Возвращает список с заявками (parser_order)
    def get_orders(self) -> list[ManualParserOrder]:
        return self.__orders

    # Удаляет выбранный treeWidgetItem
    def remove_selected_order(self):
        items = self.__tree_widget.selectedItems()
        for item in items:
            self.__tree_widget.invisibleRootItem().removeChild(item)
            for order in self.__orders:
                if item == order:
                    self.__orders.remove(order)

    # Устанавливает цвет для treeWidgetItem
    @staticmethod
    def set_order_status(order: ManualParserOrder, color: str):
        tree_widget_item = order.get_tree_widget_item()
        color = QColor(color)
        tree_widget_item.setBackground(0, color)
        tree_widget_item.setBackground(1, color)
        tree_widget_item.setBackground(2, color)
