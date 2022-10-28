from storage import Storage
from time import sleep
from comtypes.client import CreateObject
from PyPDF2 import PdfFileReader, PdfFileWriter


class DocToPdf(Storage):
    def __init__(self, stock_dir_folder):
        self.files_path = stock_dir_folder
        self.__my_files = self.get_path_docs(self.files_path)  # storage function

    def convert_word_to_pdf(self):
        for input_file in self.__my_files:
            print(f'Обработка файла: {input_file}')
            in_file = f'{self.files_path}\\{input_file}'
            out_file = f'{self.files_path}\\{self.__replace_doc_to_pdf(input_file)}'
            # create COM object
            word = CreateObject('Word.Application')
            # convert docx file  to pdf file
            doc = word.Documents.Open(in_file)  # open docx file
            doc.SaveAs(out_file, FileFormat=17)  # conversion wdFormatPDF = 17
            doc.Close()  # close docx file
            word.Quit()  # close Word Application
            sleep(3)
            # print('Добавление водяного знака')
            # self.add_watermark(out_file)

    @staticmethod
    def __replace_doc_to_pdf(file_name: str) -> str:
        if '.docx' in file_name:
            return file_name.replace('.docx', '.pdf')
        else:
            return file_name.replace('.doc', '.pdf')

    def add_watermark(self, pdf_file_path: str):
        merged = pdf_file_path.replace('.pdf', '-watermark.pdf')
        with open(pdf_file_path, "rb") as input_file:
            input_pdf = PdfFileReader(input_file, strict=False)
            watermark = self.get_orient_pdf(input_pdf.getPage(0).mediabox)
            with open(watermark, "rb") as watermark_file:
                watermark_pdf = PdfFileReader(watermark_file, strict=False)
                watermark_page = watermark_pdf.getPage(0)

                output = PdfFileWriter()

                for i in range(input_pdf.getNumPages()):
                    pdf_page = input_pdf.getPage(i)
                    pdf_page.mergePage(watermark_page)
                    output.addPage(pdf_page)

                with open(merged, "wb"):
                    output.write(merged)

    @staticmethod
    def get_orient_pdf(input_pdf) -> str:
        if input_pdf.getUpperRight_x() - input_pdf.getUpperLeft_x() > input_pdf.getUpperRight_y() - input_pdf.getLowerRight_y():
            print('horizontal')
            return 'E:\\Калиброн\\ГОСРЕЕСТР\\Стойки, кронциркули, уровни, угольники\\test\\ЧЕРНОВИК-HORIZONTAL.pdf'
        else:
            print('vertical')
            return 'E:\\Калиброн\\ГОСРЕЕСТР\\Стойки, кронциркули, уровни, угольники\\test\\ЧЕРНОВИК-VERTICAL.pdf'
