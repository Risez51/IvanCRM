from dataclasses import dataclass
from typing import Any

@dataclass
class Product:
    def __init__(self):
        self.__params = {'article': '',
                         'name': '',
                         'unit': '',
                         'purchase_price': '',
                         'quantity': '',
                         'rrc': '',
                         'roc': '',
                         'brand': '',
                         'selling_price': '',
                         'group_code': '',
                         'site_name': '',
                         'multiplicity': ''}

    def set_value(self, key_name: str, value: Any):
        self.__params[key_name] = value

    def get_params(self):
        return self.__params

    def set_article(self, value):
        self.__params['article'] = str(value)

    def set_name(self, value):
        self.__params['name'] = str(value)

    def set_unit(self, value):
        self.__params['unit'] = str(value)

    def set_purchase_price(self, value):
        self.__params['purchase_price'] = float(value)

    def set_quantity(self, value):
        self.__params['quantity'] = str(value)

    def set_rrc(self, value):
        self.__params['rrc'] = float(value)

    def set_roc(self, value):
        self.__params['roc'] = float(value)

    def set_brand(self, value):
        self.__params['brand'] = str(value)

    def set_selling_price(self, value):
        self.__params['selling_price'] = float(value)

    def set_group_code(self, value):
        self.__params['group_code'] = int(value)

    def set_site_name(self, value):
        self.__params['site_name'] = str(value)

    def set_multiplicity(self, value):
        self.__params['multiplicity'] = int(value)
