from view.user_console_interaction import UserConsoleInteraction
from parsers.result_product import Product
from parsers import parser_a4


def main():
    # UserConsoleInteraction().start()
    parser_a4.ParserA4().parse()


if __name__ == '__main__':
    main()
