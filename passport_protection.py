from docToPdf import DocToPdf
from pdfToJpg import PdfToJpg
from imgToPdf import ImgToPdf
from watermark_for_pdf import Watermark
from storage import Storage


class PassportProtection:
    def __init__(self, input_files_path: str):
        self.input_files_path = input_files_path

    def start(self):
        input_files = Storage.get_files_name(self.input_files_path)
        template_pdf_files = self.input_files_path + '\\template_pdf'
        Storage().create_folder(template_pdf_files)

        for current_file in input_files:
            DocToPdf(self.input_files_path, template_pdf_files).convert(current_file)

        output_files = Storage().get_files_name(template_pdf_files)
        template_jpg_files = self.input_files_path + '\\template_jpg'
        result_pdf_path = self.input_files_path + '\\Паспорта с защитой'
        Storage().create_folder(result_pdf_path)
        for current_file in output_files:
            print(f'Обработка файла: {current_file}')
            Storage().create_folder(template_jpg_files)
            Watermark(f'{template_pdf_files}\\{current_file}').add_watermark()
            PdfToJpg(f'{template_pdf_files}\\{current_file}', template_jpg_files).convert()
            ImgToPdf(template_jpg_files, result_pdf_path, current_file).convert()
            Storage().delete_folder_with_files(template_jpg_files)
        Storage().delete_folder_with_files(template_pdf_files)
        print(f'Обработка завершена, файлы находятся в папке {result_pdf_path}')
