from actions.passport_protection import PassportProtection
from actions.prepare_photo_archive import PreparePhotoArchive


class UserConsoleInteraction:
    def __init__(self):
        print('Введите номер(только цифру) нужного действия')
        print('#1 - Подготовить архив с фотографиями')
        print('#2 - Подготовить паспорта с защитой от копирования')
        print('#0 - Завершение работы программы\n')

    def start(self):
        action_number = input('Введите номер: ')
        self.__get_action(action_number)

    def __get_action(self, action_value: str):
        actions = {'1': self.__get_prepare_photo_archive,
                   '2': self.__get_passport_protection,
                   '0': exit}
        if action_value in actions:
            return actions[action_value]()
        else:
            print('Такого действия нет')
            return self.start()

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
