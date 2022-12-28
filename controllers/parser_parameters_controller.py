from PyQt5 import QtWidgets

from view.parsing_parameters import ParsingParametersUi
from configs import config
from parsers.headers import Headers


class ParsingParameterController:
    def __init__(self, ui: ParsingParametersUi):
        super().__init__()
        self.ui = ui
        self.ui.suppliers_combobox.addItems(config.SUPPLIERS)
        self.ui.choose_supplier_push_button.clicked.connect(self.choose_supplier)
        self.headers = config.VOID_HEADERS

    def choose_supplier(self):
        selected_supplier_item = self.ui.suppliers_combobox.currentText()
        self.headers = Headers(selected_supplier_item)
        self.__clear_all_line_edits()
        self.__fill_line_edits(self.headers)
        self.ui.article_line_edit.textChanged.connect(self.on_changed_line_edit_value)

    def __fill_line_edits(self, supplier_headers: Headers):
        self.__fill_line_edit(self.ui.article_line_edit, supplier_headers.article)
        self.__fill_line_edit(self.ui.name_line_edit, supplier_headers.name)
        self.__fill_line_edit(self.ui.unit_line_edit, supplier_headers.unit)
        self.__fill_line_edit(self.ui.purchace_price_line_edit, supplier_headers.purchase_price)
        self.__fill_line_edit(self.ui.quantity_line_edit, supplier_headers.quantity)
        self.__fill_line_edit(self.ui.rrc_line_edit, supplier_headers.rrc)
        self.__fill_line_edit(self.ui.roc_line_edit, supplier_headers.roc)
        self.__fill_line_edit(self.ui.brand_line_edit, supplier_headers.brand)
        self.__fill_line_edit(self.ui.selling_price_line_edit, supplier_headers.selling_price)
        self.__fill_line_edit(self.ui.group_key_line_edit, supplier_headers.group_key)
        self.__fill_line_edit(self.ui.site_name_line_edit, supplier_headers.site_name)
        self.__fill_line_edit(self.ui.multiplicity_line_edit, supplier_headers.multiplicity)

    def __clear_all_line_edits(self):
        self.ui.article_line_edit.clear()
        self.ui.name_line_edit.clear()
        self.ui.unit_line_edit.clear()
        self.ui.purchace_price_line_edit.clear()
        self.ui.quantity_line_edit.clear()
        self.ui.rrc_line_edit.clear()
        self.ui.roc_line_edit.clear()
        self.ui.brand_line_edit.clear()
        self.ui.selling_price_line_edit.clear()
        self.ui.group_key_line_edit.clear()
        self.ui.site_name_line_edit.clear()
        self.ui.multiplicity_line_edit.clear()

    @staticmethod
    def __fill_line_edit(line_edit: QtWidgets.QLineEdit, header: str):
        if header is None or len(header.strip()) == 0:
            line_edit.setEnabled(False)
        else:
            line_edit.setEnabled(True)
            line_edit.setText(header)

    def on_changed_line_edit_value(self):
        color1 = 'QLineEdit {background: ' + config.STATUS_PROCESSING_COLOR + ';}'
        color2 = 'QLineEdit {background: ' + config.STATUS_NONE + ';}'
        if self.ui.article_line_edit.text() != self.headers.article:
            self.ui.article_line_edit.setStyleSheet(color1)
        else:
            self.ui.article_line_edit.setStyleSheet(color2)
