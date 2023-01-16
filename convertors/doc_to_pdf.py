"""
    Searches for .doc, .docx, .pdf format files.
    Converts .doc, .docx to .pdf and places it in the resulting directory.
    Also copies .pdf files to the resulting directory
"""

from file_manager.storage import Storage
from comtypes.client import CreateObject


class DocToPdf:
    def __init__(self, input_file_path: str, output_dir_path: str):
        self.__input_file_path = input_file_path
        self.__output_dir_path = output_dir_path

    def convert(self, file_name: str):
        self.__checking_format_file(file_name)

    def __checking_format_file(self, file_name: str):
        if file_name.endswith('.docx') or file_name.endswith('.doc'):
            self.__word_to_pdf(file_name)
        elif '.pdf' in file_name:
            Storage().copy_file_to(f'{self.__input_file_path}\\{file_name}', f'{self.__output_dir_path}\\{file_name}')

    def __word_to_pdf(self, doc_file_name: str):
        word = CreateObject('Word.Application')
        in_file = f'{self.__input_file_path}\\{doc_file_name}'
        out_file = f'{self.__output_dir_path}\\{self.__replace_name_doc_to_pdf(doc_file_name)}'
        doc = word.Documents.Open(in_file)
        doc.SaveAs(out_file, FileFormat=17)
        doc.Close()
        word.Quit()

    @staticmethod
    def __replace_name_doc_to_pdf(file_name: str) -> str:
        return file_name.replace('.docx', '.pdf') if file_name.endswith('.docx') else file_name.replace('.doc', '.pdf')

