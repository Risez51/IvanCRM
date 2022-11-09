import urllib.request
from os import listdir, remove, path, rename, mkdir
from xml.dom import minidom
from shutil import move, copyfile, rmtree
from typing import List

from pandas import ExcelFile, read_csv, DataFrame
import openpyxl

from file_manager.decorator import is_exists, is_not_exists


class Storage:

    def get_dataframe(self, filepath_or_url: str, sheet_index: int = 0, start_row: int = 0) -> DataFrame:
        if filepath_or_url.startswith('http'):
            if filepath_or_url.endswith('.csv'):
                return self.__get_dataframe_from_csv_downloaded(filepath_or_url)
            else:
                return self.__get_dataframe_from_xls_downloaded(filepath_or_url, sheet_index, start_row)
        else:
            if filepath_or_url.endswith('.csv'):
                return self.__get_dataframe_from_csv(filepath_or_url)
            else:
                return self.__get_dataframe_from_excel(filepath_or_url, sheet_index, start_row)

    def __get_dataframe_from_csv_downloaded(self, url: str,
                                            sep: str = ';',
                                            encoding: str = 'latin-1') -> DataFrame:
        return read_csv(self.get_downloaded_file_to_read(url), sep=sep, engine='python', encoding=encoding)

    def __get_dataframe_from_xls_downloaded(self, url: str, sheet_index: int = 0, start_row: int = 0) -> DataFrame:
        return ExcelFile(self.get_downloaded_file_to_read(url)).parse(sheet_name=sheet_index,
                                                                      encoding_override='CORRECT_ENCODING',
                                                                      skiprows=start_row)

    def get_xml_file(self, url: str) -> minidom.Document:
        dom = minidom.parseString(self.get_downloaded_file_to_read(url))
        dom.normalize()
        return dom

    # get filenames list .doc, .docx, .pdf format
    def get_passport_type_files(self, dir_path: str):
        return [filename for filename in self.get_filenames(dir_path)
                if filename.endswith('.pdf')
                or filename.endswith('.doc')
                or filename.endswith('.docx')]

    # get data array from .xls/.xlsx file
    @staticmethod
    def __get_dataframe_from_excel(file_path: str, sheet_index: int, start_row: int) -> DataFrame:
        return ExcelFile(file_path).parse(sheet_name=sheet_index,
                                          encoding_override='CORRECT_ENCODING',
                                          skiprows=start_row)

    # return list with data from .csv file
    @staticmethod
    @is_exists
    def __get_dataframe_from_csv(file_path: str) -> DataFrame:
        return read_csv(file_path,
                        sep=";",
                        engine='python',
                        encoding='latin-1')

    # download file for read
    @staticmethod
    def get_downloaded_file_to_read(link):
        try:
            downloaded_file = urllib.request.urlopen(link)
            return downloaded_file.read()
        except ConnectionError:
            print(f'Ссылка не доступна: {link}')

    # import data(list, dict, dataframe) to xl file format
    @staticmethod
    def to_excel(my_data, filename):
        DataFrame(data=my_data).to_excel(filename, index=False)

    # return list with dir_names and file_names
    @staticmethod
    @is_exists
    def get_filenames(dir_path: str) -> List[str]:
        return listdir(dir_path)

    # return filename by file_path
    @staticmethod
    @is_exists
    def get_filename(file_path: str) -> str:
        return path.basename(file_path)

    # remove folder(folder_name) from 'from_dir' to 'to_dir'
    @staticmethod
    def move(from_dir, to_dir, name):
        if path.exists(from_dir) and path.exists(to_dir):
            move(f'{from_dir}\\{name}', to_dir)

    # copy file from "from_dir" to "to_dir"
    @staticmethod
    def copy_file_to(from_dir: str, to_dir: str):
        if path.exists(from_dir):
            copyfile(from_dir, to_dir)

    @staticmethod
    @is_exists
    def remove(file_path: str):
        remove(file_path)

    @staticmethod
    def rename(old_path_name: str, new_path_name: str):
        if path.exists(old_path_name):
            rename(old_path_name, new_path_name)

    @staticmethod
    @is_not_exists
    def create_folder(path_to: str):
        mkdir(path_to)

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

    @staticmethod
    def replace_xl_to_chk(filename: str) -> str:
        return filename.replace('.xlsx', '.chk')
