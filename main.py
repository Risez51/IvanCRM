from view.user_console_interaction import UserConsoleInteraction
from parsers.product import Product
from parsers import parser_a4, parser_torg7, parsing_parameters, parser_kvt
from file_manager.storage import Storage


def main():
    # UserConsoleInteraction().start()
    # b = parser_torg7.ParserTorg7().get_result()
    # Storage().to_excel(b, 'torgs7.xlsx')
    # print(parsing_parameters.KVT_LINK)
    parser_kvt.ParserKVT().parse_dataframe()


if __name__ == '__main__':
    main()
