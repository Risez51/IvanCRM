from xml.dom import minidom


class XmlParser:

    @staticmethod
    def get_elements_by_tag_name(dom: minidom.Document, element_name: str) -> list[minidom.Element]:
        return dom.getElementsByTagName(element_name)

    @staticmethod
    def set_article_product(node, product):
        if node.firstChild:
            product.set_article(str(node.firstChild.data))

    @staticmethod
    def set_name_product(node, product):
        if node.firstChild:
            name = str(node.firstChild.data)
            product.set_name(name)
            product.set_site_name(name)

    @staticmethod
    def set_unit_product(node, product):
        if node.firstChild:
            product.set_unit(node.firstChild.data)

    @staticmethod
    def set_purchase_price_product(node, product):
        if node.firstChild:
            product.set_purchase_price(float(node.firstChild.data))

    @staticmethod
    def set_quantity_product(node, product):
        if node.firstChild:
            product.set_quantity(int(node.firstChild.data))
