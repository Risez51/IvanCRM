from configs import config
from PyQt5.QtWidgets import QFileDialog
from os.path import abspath


class FileDialog:

    @staticmethod
    def get_file_name(types: str = config.PRICE_FILE_TYPES) -> str:
        opened_file = QFileDialog.getOpenFileName(None, 'Выберите файл', '', types)
        if opened_file[0]:
            return abspath(opened_file[0])

    @staticmethod
    def get_file_names(types: str = config.PRICE_FILE_TYPES) -> list[str]:
        opened_files = QFileDialog.getOpenFileNames(None, 'Выберите файлы', '', types)
        if opened_files[0]:
            return [abspath(file) for file in opened_files[0]]

    @staticmethod
    def get_dir_path() -> str:
        dir_location = QFileDialog.getExistingDirectory(None, 'Выберите папку')
        if dir_location:
            return abspath(dir_location)
