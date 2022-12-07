from view.user_console_interaction import UserConsoleInteraction
from file_manager.storage import Storage
from parsers.parser_torg2 import ParserTorg2
from actions.supplier_parser import SupplierParser


def main():
    #UserConsoleInteraction().start()
    SupplierParser('C:/Users/OperTech/Desktop/тест/Торг2_ЧК').create_torg2()


if __name__ == '__main__':
    main()
