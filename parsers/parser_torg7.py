from parsers.product import Product
from file_manager.storage import Storage
from parsers.base_parser import XmlParser
from configs import config


class ParserTorg7(XmlParser):

    def __init__(self, file_path):
        self.xml_link = file_path
        if self.xml_link == '':
            self.xml_link = config.TOG7_LINK
        self.headers = config.TORG7_HEADERS

    def get_result(self):
        xml_file = Storage().get_xml_file(self.xml_link)
        items = self.get_elements_by_tag_name(xml_file, 'item')
        return self.__get_products_list(items)

    def __get_products_list(self, items):
        products = []
        for item in items:
            product = Product()
            for node in item.childNodes:
                if node.nodeType == 1:
                    self.__set_product_values(node, product)
            if self.__is_product(product):
                products.append(product.get_params())
        return products

    def __set_product_values(self, node, product):
        if node.tagName == self.headers.article:
            self.set_article_product(node, product)
        elif node.tagName == self.headers.purchase_price:
            self.__set_product_prices(node, product)
        elif node.tagName == self.headers.name:
            self.set_name_product(node, product)
        elif node.tagName == self.headers.unit:
            self.set_unit_product(node, product)
        elif node.tagName == self.headers.quantity:
            self.set_quantity_product(node, product)

    @staticmethod
    def __is_product(product):
        return False if 'крин' in product.get_params()['Наименование'].lower() else True

    @staticmethod
    def __set_product_prices(node, product):
        if node.firstChild:
            purchase_price = float(node.firstChild.data) / config.NDS
            selling_price = purchase_price * config.TORG7_MARGIN
            product.set_purchase_price(purchase_price)
            product.set_selling_price(selling_price)
