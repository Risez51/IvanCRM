"""
    Accepts the path to a .pdf file.
    Specifies the page orientation of the .pdf file.
    Adds a watermark to a .pdf file
"""

from PyPDF2 import PdfFileReader, PdfFileWriter, PageObject
from file_manager.storage import Storage


class Watermark:
    def __init__(self, input_file_path: str):
        self.path_to_pdf_file = input_file_path

    def add_watermark(self):
        result_pdf_path_name = self.path_to_pdf_file.replace('.pdf', '-watermark.pdf')
        input_pdf_file = self.__get_pdf_for_read(self.path_to_pdf_file)
        watermark_page = self.__get_orient_watermark_pdf(self.path_to_pdf_file)
        output = PdfFileWriter()

        for i in range(input_pdf_file['reader'].getNumPages()):
            input_pdf_page = input_pdf_file['reader'].getPage(i)
            input_pdf_page.mergePage(watermark_page)
            output.addPage(input_pdf_page)

        self.__write_pdf(result_pdf_path_name, output)
        input_pdf_file['file'].close()
        Storage().remove(self.path_to_pdf_file)
        Storage().rename(result_pdf_path_name, self.path_to_pdf_file)

    # get the watermark of the desired orientation
    def __get_orient_watermark_pdf(self, input_pdf: str) -> PageObject:
        input_pdf = self.__get_first_page_of_pdf(input_pdf).mediabox
        if input_pdf.getUpperRight_x() - input_pdf.getUpperLeft_x() > \
                input_pdf.getUpperRight_y() - input_pdf.getLowerRight_y():
            return self.__get_first_page_of_pdf('../work_files/ЧЕРНОВИК-HORIZONTAL.pdf')
        else:
            return self.__get_first_page_of_pdf('../work_files/ЧЕРНОВИК-VERTICAL.pdf')

    # get watermark page
    def __get_first_page_of_pdf(self, file_path: str) -> PageObject:
        pdf_file = self.__get_pdf_for_read(file_path)
        return pdf_file['reader'].getPage(0)

    @staticmethod
    def __get_pdf_for_read(file_path: str) -> dict:
        opened_file = open(file_path, 'rb')
        return {'reader': PdfFileReader(opened_file, strict=False),
                'file': opened_file}

    @staticmethod
    def __write_pdf(file_path: str, stream: PdfFileWriter):
        with open(file_path, 'wb'):
            stream.write(file_path)
