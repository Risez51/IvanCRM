from actions.passport_protection import PassportProtection
from actions.prepare_photo_archive import PreparePhotoArchive
from actions.supplier_parser import SupplierParser
import os
import sys


class UserConsoleInteraction:

    def start(self):
        os.system('cls')
        self.print_start_info()
        action_number = input('Введите номер: ')
        self.__get_action(action_number)

    def __get_action(self, action_value: str):
        actions = {'1': self.__get_prepare_photo_archive,
                   '2': self.__get_passport_protection,
                   '3': self.__parse_suppliers,
                   '0': sys.exit}
        if action_value in actions:
            return actions[action_value]()
        else:
            print('Такого действия нет')
            return self.start()

    def __parse_suppliers(self):
        self.__print_parsing_info()
        action = input('Введите номер:')
        if action == '0':
            self.start()
        else:
            self.__get_parse_action(action)

    def __get_parse_action(self, action_value: str):
        output_path = input('Введите путь к каталогу для итоговых файлов:')
        sp = SupplierParser(output_path)
        actions = {'1': sp.create_a4,
                   '2': sp.create_kvt,
                   '3': sp.create_torg7,
                   '4': sp.create_all}

        if action_value in actions:
            return actions[action_value]()
        else:
            print('Такого действия нет')
            return self.__parse_suppliers()

    @staticmethod
    def __get_prepare_photo_archive():
        dir_with_photo_path = input('Введите путь к папке с архивом фото:')
        file_with_articles_path = input('Введите путь к файлу с артикулами без фото:')
        result_dir_path = input('Введите путь к папке, где будет результат:')
        PreparePhotoArchive(dir_with_photo_path, file_with_articles_path, result_dir_path).start()

    @staticmethod
    def __get_passport_protection():
        dir_with_passports = input('Введите путь к папке с паспортами:')
        PassportProtection(dir_with_passports).start()

    @staticmethod
    def print_start_info():
        print('Введите номер(только цифру) нужного действия')
        print('#1 - Подготовить архив с фотографиями')
        print('#2 - Подготовить паспорта с защитой от копирования')
        print('#3 - Парсинг прайсов сторонних поставщиков')
        print('#0 - Завершение работы программы\n')

    @staticmethod
    def __print_parsing_info():
        print('#1 - Парсинг А4_ИД')
        print('#2 - Парсинг КВТ_СИТ')
        print('#3 - Парсинг ТОРГ7_ЧК')
        print('#4 - Парсинг всех вышеперечисленных')
        print('#0 - Вернуться назад')
