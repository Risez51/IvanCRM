from configs.config_worker import ConfigReader


class Headers:
    def __init__(self, supplier_name: str):
        self.__headers = ConfigReader().get_supplier_headers(supplier_name)
        self.article = self.__headers['Артикул']
        self.name = self.__headers['Наименование']
        self.unit = self.__headers['Ед.изм']
        self.quantity = self.__headers['Количество']
        self.purchase_price = self.__headers['Цена поставки, б/ндс']
        self.rrc = self.__headers['РРЦ']
        self.roc = self.__headers['РОЦ']
        self.brand = self.__headers['Бренд']
        self.selling_price = self.__headers['Цена продажи, б/ндс']
        self.group_key = self.__headers['Код группы']
        self.site_name = self.__headers['Наименование для сайтов']
        self.multiplicity = self.__headers['Кратность']

    # ПОКА ЧТО НЕ ИСПОЛЬЗУЮТСЯ ГЕТТЕРЫ
    def get_name(self) -> str:
        return self.__headers['Наименование']

    def get_article(self) -> str:
        return self.__headers['Артикул']

    def get_unit(self) -> str:
        return self.__headers['Ед.изм']

    def get_purchase_price(self) -> str:
        return self.__headers['Цена поставки, б/ндс']

    def get_quantity(self) -> str:
        return self.__headers['Количество']

    def get_rrc(self) -> str:
        return self.__headers['РРЦ']

    def get_roc(self) -> str:
        return self.__headers['РОЦ']

    def get_brand(self) -> str:
        return self.__headers['Бренд']

    def get_selling_price(self) -> str:
        return self.__headers['Цена продажи, б/ндс']

    def get_group_key(self) -> str:
        return self.__headers['Код группы']

    def get_site_name(self) -> str:
        return self.__headers['Наименование для сайтов']

    def get_multiplicity(self) -> str:
        return self.__headers['Кратность']

