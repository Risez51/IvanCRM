from storage import Storage
from comtypes.client import CreateObject


class DocToPdf(Storage):
    def __init__(self, input_file_path: str, output_dir_path: str):
        self.input_file_path = input_file_path
        self.output_dir_path = output_dir_path

    def convert(self, file_name: str):
        self.__checking_format_file(file_name)

    def __checking_format_file(self, file_name: str):
        if '.doc' in file_name and not '$' in file_name:
            self.__word_to_pdf(file_name)
        elif '.pdf' in file_name and not '$' in file_name:
            self.copy_file_to(f'{self.input_file_path}\\{file_name}', f'{self.output_dir_path}\\{file_name}')
        else:
            print(f'Неподходящий формат файла: {file_name}')

    def __word_to_pdf(self, doc_file_name: str):
        word = CreateObject('Word.Application')
        print(f'Обработка файла: {doc_file_name}\n Процесс...')
        in_file = f'{self.input_file_path}\\{doc_file_name}'
        out_file = f'{self.output_dir_path}\\{self.__replace_name_doc_to_pdf(doc_file_name)}'
        doc = word.Documents.Open(in_file)
        doc.SaveAs(out_file, FileFormat=17)
        doc.Close()
        word.Quit()

    @staticmethod
    def __replace_name_doc_to_pdf(file_name: str) -> str:
        return file_name.replace('.docx', '.pdf') if file_name.endswith('.docx') else file_name.replace('.doc', '.pdf')

