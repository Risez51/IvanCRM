import json


class ConfigReader:
    def __init__(self):
        with open(r'C:\Users\OperTech\pythonProject\IvanCRM\configs\settings_parser.json',
                  'r',
                  encoding='utf-8') as json_file:
            self.config_reader = json.load(json_file)

    def get_supplier_name(self, supplier_name):
        return self.config_reader['supplier_names'][supplier_name]

    def get_supplier_names(self) -> list[str]:
        try:
            return self.config_reader['supplier_names'].values()
        except KeyError:
            print('В settings_parser.ini отсутсвует список поставщиков')

    def get_supplier_headers(self, supplier_name: str) -> dict:
        try:
            return self.config_reader['supplier_headers'][supplier_name]
        except KeyError:
            print(f'У поставщика {supplier_name} - нет заголовков')

    def get_supplier_margin(self, supplier_name: str) -> float:
        try:
            return self.config_reader['supplier_margins'][supplier_name]
        except KeyError:
            print(f'У поставщика {supplier_name} - нет коэффициента наценки')
            return 1

    def get_supplier_needful_brands(self, supplier_name: str) ->list[str]:
        try:
            return self.config_reader['supplier_brand_needful'][supplier_name]
        except KeyError:
            print(f'У поставщика {supplier_name} - не указаны необходимые для парсинга бренды')
            return []

    def get_supplier_exception_brands(self, supplier_name: str) -> list[str]:
        try:
            return self.config_reader['supplier_brand_exceptions'][supplier_name]
        except KeyError:
            print(f'У поставщика {supplier_name} нет брендов-исключений')
            return []

    def get_taxes(self, taxes_name):
        try:
            return self.config_reader['taxes'][taxes_name]
        except KeyError:
            print(f'Не существует параметра-налога {taxes_name}')
            return 1

    def get_supplier_link(self, supplier_name: str) -> str:
        try:
            return self.config_reader['supplier_links'][supplier_name]
        except KeyError:
            print(f'У поставщика {supplier_name} - нет ссылки')
            return ''
