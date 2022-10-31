from pandas import ExcelFile, read_csv
from shutil import move, copyfile
import openpyxl
from os import listdir, remove
from typing import List
from numpy import array

class Storage:
    # get data array from .csv/excel file
    def get_data_list(self, file_path: str, sheet_index: int = 0) -> array:
        return self.__get_data_from_excel(file_path, sheet_index) if ".xl" in file_path \
            else self.__get_list_from_csv(file_path)

    # get data array from .xls/.xlsx file
    @staticmethod
    def __get_data_from_excel(file_path: str, sheet_index: int) -> array:
        return ExcelFile(file_path).parse(sheet_name=sheet_index, encoding_override='CORRECT_ENCODING').to_numpy()

    # return list with data from .csv file
    @staticmethod
    def __get_list_from_csv(file_path: str) -> array:
        return read_csv(file_path, sep=";", engine='python', encoding='latin-1').to_numpy()

    # return list with files name .doc format
    def get_docs_name(self, dir_path: str) -> List[str]:
        return [doc_file_path for doc_file_path in self.get_files_name(dir_path) if '.doc' in doc_file_path and not '$' in doc_file_path]

    # return list with files name .pdf format
    def get_pdfs_name(self, dir_path: str) -> List[str]:
        return [doc_file_path for doc_file_path in self.get_files_name(dir_path) if '.pdf' in doc_file_path and not '$' in doc_file_path]

    # return list with dir_names and file_names
    @staticmethod
    def get_files_name(dir_path: str) -> List[str]:
        return listdir(dir_path)

    # remove folder(folder_name) from 'from_dir' to 'to_dir'
    @staticmethod
    def move(from_dir, to_dir, name):
        move(f'{from_dir}\\{name}', to_dir)

    @staticmethod
    def copy_file_to(from_dir, to_dir):
        copyfile(from_dir, to_dir)

    @staticmethod
    def remove(file_path):
        remove(file_path)
