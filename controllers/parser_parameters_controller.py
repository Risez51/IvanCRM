from PyQt5 import QtWidgets

from view.parsing_parameters import ParsingParametersUi
from configs import config
from configs.config_worker import ConfigUpdater
from parsers.headers import Headers


class ParsingParameterController:
    def __init__(self, ui: ParsingParametersUi):
        super().__init__()
        self.ui = ui
        # Connectors
        self.ui.choose_supplier_push_button.clicked.connect(self.choose_supplier)
        self.ui.save_push_button.clicked.connect(self.on_save_push_button)
        self.ui.cancel_push_button.clicked.connect(self.on_cancel_push_button)
        # Headers (default = VOID)
        self.headers = config.VOID_HEADERS
        # Fill combobox items
        self.ui.suppliers_combobox.addItems(config.SUPPLIERS)

    def on_save_push_button(self):
        supplier_name = self.ui.suppliers_combobox.currentText()
        config_updater = ConfigUpdater()
        config_updater.update_supplier_headers(supplier_name,
                                               self.ui.article_line_edit.text(),
                                               self.ui.name_line_edit.text(),
                                               self.ui.unit_line_edit.text(),
                                               self.ui.purchace_price_line_edit.text(),
                                               self.ui.quantity_line_edit.text(),
                                               self.ui.rrc_line_edit.text(),
                                               self.ui.roc_line_edit.text(),
                                               self.ui.brand_line_edit.text(),
                                               self.ui.selling_price_line_edit.text(),
                                               self.ui.group_key_line_edit.text(),
                                               self.ui.site_name_line_edit.text(),
                                               self.ui.multiplicity_line_edit.text()
                                               )
        config_updater.update_json()
        self.choose_supplier()

    def on_cancel_push_button(self):
        self.ui.close()

    def choose_supplier(self):
        selected_supplier_item = self.ui.suppliers_combobox.currentText()
        self.headers = Headers(selected_supplier_item)
        self.__clear_all_line_edits()
        self.__fill_all_line_edits(self.headers)
        self.__connect_line_edit_changed()

    def __fill_all_line_edits(self, supplier_headers: Headers):
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

    def __connect_line_edit_changed(self):
        self.ui.article_line_edit.textChanged.connect(
            lambda: self.on_line_edit_text_changed(self.ui.article_line_edit,
                                                   self.headers.article))
        self.ui.name_line_edit.textChanged.connect(
            lambda: self.on_line_edit_text_changed(self.ui.name_line_edit,
                                                   self.headers.name))
        self.ui.unit_line_edit.textChanged.connect(
            lambda: self.on_line_edit_text_changed(self.ui.unit_line_edit,
                                                   self.headers.unit))
        self.ui.purchace_price_line_edit.textChanged.connect(
            lambda: self.on_line_edit_text_changed(self.ui.purchace_price_line_edit,
                                                   self.headers.purchase_price))
        self.ui.quantity_line_edit.textChanged.connect(
            lambda: self.on_line_edit_text_changed(self.ui.quantity_line_edit,
                                                   self.headers.quantity))
        self.ui.rrc_line_edit.textChanged.connect(
            lambda: self.on_line_edit_text_changed(self.ui.rrc_line_edit,
                                                   self.headers.rrc))
        self.ui.roc_line_edit.textChanged.connect(
            lambda: self.on_line_edit_text_changed(self.ui.roc_line_edit,
                                                   self.headers.roc))
        self.ui.brand_line_edit.textChanged.connect(
            lambda: self.on_line_edit_text_changed(self.ui.brand_line_edit,
                                                   self.headers.brand))
        self.ui.selling_price_line_edit.textChanged.connect(
            lambda: self.on_line_edit_text_changed(self.ui.selling_price_line_edit,
                                                   self.headers.selling_price))
        self.ui.group_key_line_edit.textChanged.connect(
            lambda: self.on_line_edit_text_changed(self.ui.group_key_line_edit,
                                                   self.headers.group_key))
        self.ui.site_name_line_edit.textChanged.connect(
            lambda: self.on_line_edit_text_changed(self.ui.site_name_line_edit,
                                                   self.headers.site_name))
        self.ui.multiplicity_line_edit.textChanged.connect(
            lambda: self.on_line_edit_text_changed(self.ui.multiplicity_line_edit,
                                                   self.headers.multiplicity))

    @staticmethod
    def on_line_edit_text_changed(line_edit: QtWidgets.QLineEdit, header: str):
        color_changed = 'QLineEdit {background: ' + config.STATUS_PROCESSING_COLOR + ';}'
        color_no_changed = 'QLineEdit {background: ' + config.STATUS_NONE + ';}'
        if line_edit.text() != header:
            line_edit.setStyleSheet(color_changed)
        else:
            line_edit.setStyleSheet(color_no_changed)
