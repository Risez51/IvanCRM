import json
from configs import config


class ConfigReader:
    def __init__(self):
        with open(config.SETTINGS_JSON,
                  'r',
                  encoding='utf-8') as json_file:
            self.json_data = json.load(json_file)

    def get_supplier_name(self, supplier_name):
        return self.json_data['supplier_names'][supplier_name]

    def get_supplier_names(self) -> list[str]:
        try:
            return self.json_data['supplier_names'].values()
        except KeyError:
            print('В settings_parser.ini отсутсвует список поставщиков')

    def get_supplier_headers(self, supplier_name: str) -> dict:
        try:
            return self.json_data['supplier_headers'][supplier_name]
        except KeyError:
            print(f'У поставщика {supplier_name} - нет заголовков')

    def get_supplier_margin(self, supplier_name: str):
        try:
            return self.json_data['supplier_margins'][supplier_name]
        except KeyError:
            print(f'У поставщика {supplier_name} - нет коэффициента наценки')
            return ''

    def get_supplier_needful_brands(self, supplier_name: str) -> list[str]:
        try:
            return self.json_data['supplier_brand_needful'][supplier_name]
        except KeyError:
            print(f'У поставщика {supplier_name} - не указаны необходимые для парсинга бренды')
            return []

    def get_supplier_exception_brands(self, supplier_name: str) -> list[str]:
        try:
            return self.json_data['supplier_brand_exceptions'][supplier_name]
        except KeyError:
            print(f'У поставщика {supplier_name} нет брендов-исключений')
            return []

    def get_taxes(self, taxes_name):
        try:
            return self.json_data['taxes'][taxes_name]
        except KeyError:
            print(f'Не существует параметра-налога {taxes_name}')
            return ''

    def get_supplier_link(self, supplier_name: str) -> str:
        try:
            return self.json_data['supplier_links'][supplier_name]
        except KeyError:
            print(f'У поставщика {supplier_name} - нет ссылки')
            return ''


class ConfigUpdater:
    def __init__(self):
        with open(config.SETTINGS_JSON,
                  'r',
                  encoding='utf-8') as json_file:
            self.json_data = json.load(json_file)

    def update_supplier_name(self, old_name_key: str, new_name: str):
        self.json_data['supplier_names'][old_name_key] = new_name

    def update_supplier_margin(self, supplier_name: str, new_margin: str):
        self.json_data['supplier_margins'][supplier_name] = float(new_margin)

    def update_supplier_header_article(self, supplier_name: str, new_value: str):
        self.json_data['supplier_headers'][supplier_name]['Артикул'] = new_value

    def update_supplier_header_name(self, supplier_name: str, new_value: str):
        self.json_data['supplier_headers'][supplier_name]['Наименование'] = new_value

    def update_supplier_header_unit(self, supplier_name: str, new_value: str):
        self.json_data['supplier_headers'][supplier_name]['Ед.изм'] = new_value

    def update_supplier_header_purchase_price(self, supplier_name: str, new_value: str):
        self.json_data['supplier_headers'][supplier_name]['Цена поставки, б/ндс'] = new_value

    def update_supplier_header_quantity(self, supplier_name: str, new_value: str):
        self.json_data['supplier_headers'][supplier_name]['Количество'] = new_value

    def update_supplier_header_rrc(self, supplier_name: str, new_value: str):
        self.json_data['supplier_headers'][supplier_name]['РРЦ'] = new_value

    def update_supplier_header_roc(self, supplier_name: str, new_value: str):
        self.json_data['supplier_headers'][supplier_name]['РОЦ'] = new_value

    def update_supplier_header_brand(self, supplier_name: str, new_value: str):
        self.json_data['supplier_headers'][supplier_name]['Бренд'] = new_value

    def update_supplier_header_selling_price(self, supplier_name: str, new_value: str):
        self.json_data['supplier_headers'][supplier_name]['Цена продажи, б/ндс'] = new_value

    def update_supplier_header_group_key(self, supplier_name: str, new_value: str):
        self.json_data['supplier_headers'][supplier_name]['Код группы'] = new_value

    def update_supplier_header_site_name(self, supplier_name: str, new_value: str):
        self.json_data['supplier_headers'][supplier_name]['Наименование для сайтов'] = new_value

    def update_supplier_header_multiplicity(self, supplier_name: str, new_value: str):
        self.json_data['supplier_headers'][supplier_name]['Кратность'] = new_value

    def update_supplier_headers(self, sup_name: str, article: str, name: str, unit: str, purchase_price: str,
                                quantity: str, rrc: str, roc: str, brand: str, selling_price: str, group_key: str,
                                site_name: str, multiplicity: str):
        self.update_supplier_header_article(sup_name, article)
        self.update_supplier_header_name(sup_name, name)
        self.update_supplier_header_unit(sup_name, unit)
        self.update_supplier_header_purchase_price(sup_name, purchase_price)
        self.update_supplier_header_quantity(sup_name, quantity)
        self.update_supplier_header_rrc(sup_name, rrc)
        self.update_supplier_header_roc(sup_name, roc)
        self.update_supplier_header_brand(sup_name, brand)
        self.update_supplier_header_selling_price(sup_name, selling_price)
        self.update_supplier_header_group_key(sup_name, group_key)
        self.update_supplier_header_site_name(sup_name, site_name)
        self.update_supplier_header_multiplicity(sup_name, multiplicity)

    def update_json(self):
        with open(config.SETTINGS_JSON, 'w', encoding='utf-8') as json_file:
            json.dump(self.json_data, json_file, indent=2, ensure_ascii=False)
