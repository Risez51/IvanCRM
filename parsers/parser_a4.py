from parsers.result_product import Product
from file_manager.storage import Storage
import parsers.parsing_parameters as pp
from parsers.base_parser import XmlParser


class ParserA4(XmlParser):

    def __init__(self):
        self.xml_link = pp.A4_LINK
        self.__margin = 1.4

    def parse(self):
        xml_dom_file = Storage().get_xml_file(self.xml_link)
        offers = self.get_elements_by_tag_name(xml_dom_file, 'offer')
        products_list = []
        for offer in offers:
            product = Product()
            offer_id = offer.getAttribute('id')
            for node in offer.childNodes:
                if node.nodeType == 1:
                    self.set_product_values(product, node, offer_id)

            if self.is_right_product(product):
                products_list.append(product.get_params())
                break
        print(len(products_list))
        print(products_list[0])

    def set_product_values(self, product, node, offer_id):
        if node.tagName == 'vendorCode':
            self.set_article_product(node, product,  offer_id)
        elif node.tagName == 'name':
            self.set_name_product(node, product)
        elif node.tagName == 'price-dealer':
            self.set_price_product(node, product)
        elif node.tagName == 'gk_balance_available':
            self.set_quantity_product(node, product)

    @staticmethod
    def set_article_product(node, product, id_offer=''):
        if node.firstChild:
            correct_article = str(node.firstChild.data) + ' ' + str(id_offer)
            product.set_article(correct_article)

    @staticmethod
    def set_price_product(node, product):
        if node.firstChild:
            purchase_price = float(node.firstChild.data) / pp.NDS
            product.set_purchase_price(purchase_price)
            product.set_selling_price(purchase_price * pp.A4_MARGIN)

    @staticmethod
    def is_right_product(product):
        if 'AE&T' in product.get_params()['name']:
            return True
        else:
            del product
            return False
