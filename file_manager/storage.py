
from xml.dom import minidom
import urllib.request
import numpy
import os.path
import openpyxl

from pandas import ExcelFile, read_csv
from shutil import move, copyfile, rmtree
from os import listdir, remove
from typing import List
from numpy import array
from file_manager.decorator import is_exists, is_not_exists


class Storage:

    # get data array from .csv/excel file
    def get_data_from_excel(self, file_path: str, sheet_index: int = 0) -> numpy.array:
        return self.__get_data_from_excel(file_path, sheet_index) if ".xl" in file_path \
            else self.__get_list_from_csv(file_path)

    def get_passport_type_files(self, dir_path: str):
        return [filename for filename in self.get_filenames(dir_path)
                if filename.endswith('.pdf')
                or filename.endswith('.doc')
                or filename.endswith('.docx')]

    @staticmethod
    def get_xml_file(url: str) -> minidom.Document:
        try:
            xml_file = urllib.request.urlopen(url)
            xml_data_file = xml_file.read()
            dom = minidom.parseString(xml_data_file)
            dom.normalize()
            return dom
        except ConnectionError:
            print(f'Ссылка недоступна: {url}')

    # get data array from .xls/.xlsx file
    @staticmethod
    def __get_data_from_excel(file_path: str, sheet_index: int) -> array:
        return ExcelFile(file_path).parse(sheet_name=sheet_index, encoding_override='CORRECT_ENCODING').to_numpy()

    # return list with data from .csv file
    @staticmethod
    @is_exists
    def __get_list_from_csv(file_path: str) -> array:
        return read_csv(file_path, sep=";", engine='python', encoding='latin-1').to_numpy()

    # return list with dir_names and file_names
    @staticmethod
    @is_exists
    def get_filenames(dir_path: str) -> List[str]:
        return listdir(dir_path)

    # return file name
    @staticmethod
    @is_exists
    def get_filename(dir_path: str) -> str:
        return os.path.basename(dir_path)

    # remove folder(folder_name) from 'from_dir' to 'to_dir'
    @staticmethod
    def move(from_dir, to_dir, name):
        if os.path.exists(from_dir) and os.path.exists(to_dir):
            move(f'{from_dir}\\{name}', to_dir)

    # copy file from "from_dir" to "to_dir"
    @staticmethod
    def copy_file_to(from_dir, to_dir):
        if os.path.exists(from_dir):
            copyfile(from_dir, to_dir)

    @staticmethod
    @is_exists
    def remove(file_path):
        remove(file_path)

    @staticmethod
    def rename(old_path_name, new_path_name):
        if os.path.exists(old_path_name):
            os.rename(old_path_name, new_path_name)

    @staticmethod
    @is_not_exists
    def create_folder(path_to):
        os.mkdir(path_to)

    @staticmethod
    @is_exists
    def delete_file_folder(path_to: str):
        rmtree(path_to)

    @staticmethod
    def replace_doc_to_pdf_name(filename: str) -> str:
        if filename.endswith('.doc'):
            return filename.replace('.doc', '.pdf')
        elif filename.endswith('.docx'):
            return filename.replace('.docx', '.pdf')
        else:
            return filename


