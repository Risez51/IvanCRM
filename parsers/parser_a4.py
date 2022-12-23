from parsers.product import Product
from file_manager.storage import Storage
import parsers.parsing_parameters as pp
from parsers.base_parser import XmlParser


class ParserA4(XmlParser):

    def __init__(self, file_path: str):
        self.xml_link = file_path
        if self.xml_link == '':
            self.xml_link = pp.A4_LINK

    def get_result(self) -> list[dict]:
        xml_file = Storage().get_xml_file(self.xml_link)
        offers = self.get_elements_by_tag_name(xml_file, 'offer')
        return self.__get_products_list(offers)

    def __get_products_list(self, offers) -> list[dict]:
        products = []
        for offer in offers:
            product = Product()
            offer_id = offer.getAttribute('id')
            for node in offer.childNodes:
                if node.nodeType == 1:
                    self.__set_product_values(product, node, offer_id)
            if self.__is_product(product):
                products.append(product.get_params())
        return products

    def __set_product_values(self, product: Product, node, offer_id):
        if node.tagName == 'vendorCode':
            self.__set_article_product(node, product, offer_id)
        elif node.tagName == 'name':
            self.set_name_product(node, product)
        elif node.tagName == 'price-dealer':
            self.__set_price_product(node, product)
        elif node.tagName == 'gk_balance_available':
            self.set_quantity_product(node, product)

    @staticmethod
    def __set_article_product(node, product, id_offer):
        if node.firstChild:
            correct_article = str(node.firstChild.data) + ' ' + str(id_offer)
            product.set_article(correct_article)

    @staticmethod
    def __set_price_product(node, product: Product):
        if node.firstChild:
            purchase_price = float(node.firstChild.data) / pp.NDS
            product.set_purchase_price(purchase_price)
            product.set_selling_price(purchase_price * pp.A4_MARGIN)

    @staticmethod
    def __is_product(product: Product):
        if 'AE&T' in product.get_params()['Наименование']:
            return True
        else:
            del product
            return False
