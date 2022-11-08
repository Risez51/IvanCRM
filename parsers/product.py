class Product:
    def __init__(self):
        self.__params = {'Артикул': None,
                         'Наименование': None,
                         'Ед.изм': None,
                         'Цена поставки, б/ндс': None,
                         'Количество': None,
                         'РРЦ': None,
                         'РОЦ': None,
                         'Бренд': None,
                         'Цена продажи, б/ндс': None,
                         'Код группы': None,
                         'Наименование для сайтов': None,
                         'Кратность': None}

    def get_params(self):
        return self.__params

    def set_article(self, value):
        self.__params['Артикул'] = str(value)

    def set_name(self, value):
        self.__params['Наименование'] = str(value)

    def set_unit(self, value):
        self.__params['Ед.изм'] = str(value)

    def set_purchase_price(self, value):
        self.__params['Цена поставки, б/ндс'] = float(value)

    def set_quantity(self, value):
        self.__params['Количество'] = str(value)

    def set_rrc(self, value):
        self.__params['РРЦ'] = float(value)

    def set_roc(self, value):
        self.__params['РОЦ'] = float(value)

    def set_brand(self, value):
        self.__params['Бренд'] = str(value)

    def set_selling_price(self, value):
        self.__params['Цена продажи, б/ндс'] = float(value)

    def set_group_code(self, value):
        self.__params['Код группы'] = int(value)

    def set_site_name(self, value):
        self.__params['Наименование для сайтов'] = str(value)

    def set_multiplicity(self, value):
        self.__params['Кратность'] = int(value)
