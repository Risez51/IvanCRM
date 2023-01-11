import os.path


def is_exists(func):
    def wrapper(current_path):
        if os.path.exists(current_path):
            return func(current_path)
        else:
            print(f'Не существует: {current_path}')
    return wrapper


def is_not_exists(func):
    def wrapper(current_path):
        if os.path.exists(current_path):
            print(f'Уже существует: {current_path}')
        else:
            return func(current_path)
    return wrapper
