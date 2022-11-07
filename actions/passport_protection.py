"""
    Designed to convert .doc, .docx to pdf files.
    The input data can also contain ready-made .pdf files.
    Adds a watermark to .pdf.
    Converts .pdf to jpg and back to .pdf
"""

from convertors.doc_to_pdf import DocToPdf
from convertors.pdf_to_jpg import PdfToJpg
from convertors.img_to_pdf import ImgToPdf
from convertors.watermark_for_pdf import Watermark
from file_manager.storage import Storage

class PassportProtection:
    def __init__(self, input_files_path: str):
        self.__input_files_path = input_files_path
        self.__temporary_pdf_path = input_files_path + '\\temporary_pdf'
        self.__temporary_jpg_path = input_files_path + '\\temporary_jpg'
        self.__protected_pdf_path = input_files_path + '\\Паспорта с защитой'

    def start(self):
        self.__create_temporary_folders()
        incoming_passport_files = Storage().get_passport_type_files(self.__input_files_path)
        for passport_file in incoming_passport_files:
            self.__create_secure_passport(passport_file)
        Storage().delete_file_folder(self.__temporary_pdf_path)
        print(f'\nОбработка завершена, файлы находятся в папке {self.__protected_pdf_path}')

    def __create_temporary_folders(self):
        Storage().create_folder(self.__temporary_pdf_path)
        Storage().create_folder(self.__protected_pdf_path)

    def __create_secure_passport(self, passport_name: str):
        self.__prepare_pdf_file(passport_name)
        passport_pdf_name = Storage().replace_doc_to_pdf_name(passport_name)
        self.__add_watermark(passport_pdf_name)
        self.__convert_pdf_to_jpg(passport_pdf_name)
        self.__convert_jpg_to_pdf(passport_pdf_name)

    def __prepare_pdf_file(self, filename: str):
        if not filename.endswith('.pdf'):
            print(f'Преобразование: {filename}  -----> .PDF')
        DocToPdf(self.__input_files_path, self.__temporary_pdf_path).convert(filename)

    def __add_watermark(self, filename: str):
        print(f'Преобразование: {filename}  ----->  add a watermark')
        Watermark(f'{self.__temporary_pdf_path}\\{filename}').add_watermark()

    def __convert_pdf_to_jpg(self, filename: str):
        print(f"Преобразование: {filename}  -----> .JPG")
        Storage().create_folder(self.__temporary_jpg_path)
        PdfToJpg(f'{self.__temporary_pdf_path}\\{filename}', self.__temporary_jpg_path).convert()

    def __convert_jpg_to_pdf(self, filename: str):
        print(f"Преобразование: {filename.replace('.pdf', '.jpg')}  -----> .PDF\n----------------------------")
        ImgToPdf(self.__temporary_jpg_path, self.__protected_pdf_path, filename).convert()
        Storage().delete_file_folder(self.__temporary_jpg_path)
