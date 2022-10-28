import storage
import time
import comtypes.client
from PyPDF2 import PdfFileReader, PdfFileWriter


class DocToPdf:
    def __init__(self, stock_dir_folder):
        self.files_path = stock_dir_folder
        self.my_files = storage.Storage().get_path_docs(self.files_path)

    def convert_word_to_pdf(self):
        #wdFormatPDF = 17

        for input_file in self.my_files:
            print(f'Обработка файла: {input_file}')
            in_file = f'{self.files_path}\\{input_file}'
            out_file = f'{self.files_path}\\{self.replace_doc_to_pdf(input_file)}'

            # create COM object
            word = comtypes.client.CreateObject('Word.Application')
            # convert docx file  to pdf file
            doc = word.Documents.Open(in_file)  # open docx file
            doc.SaveAs(out_file, FileFormat=17)  # conversion
            doc.Close()  # close docx file
            word.Quit()  # close Word Application
            time.sleep(3)
            #print('Добавление водяного знака')
            #self.add_watermark(out_file)


    def replace_doc_to_pdf(self,file_name):
        if '.docx' in file_name:
            return file_name.replace('.docx', '.pdf')
        else:
            return file_name.replace('.doc', '.pdf')

    def add_watermark(self, pdf_file_path):
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


    def get_orient_pdf(self, input_pdf):
        if input_pdf.getUpperRight_x() - input_pdf.getUpperLeft_x() > input_pdf.getUpperRight_y() - input_pdf.getLowerRight_y():
            print('horizontal')
            return 'E:\\Калиброн\\ГОСРЕЕСТР\\Стойки, кронциркули, уровни, угольники\\test\\ЧЕРНОВИК-HORIZONTAL.pdf'
        else:
            print('vertical')
            return 'E:\\Калиброн\\ГОСРЕЕСТР\\Стойки, кронциркули, уровни, угольники\\test\\ЧЕРНОВИК-VERTICAL.pdf'
