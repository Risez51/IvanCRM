from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import RectangleObject
import storage
from storage import Storage


class Watermark:
    def __init__(self, pdf_file_path: str):
        self.pdf_file_path = pdf_file_path

    def add_watermark(self):
        # print(f'Добавление Watermark: {Storage().get_file_name(self.pdf_file_path)}')
        merged = self.pdf_file_path.replace('.pdf', '-watermark.pdf')
        with open(self.pdf_file_path, "rb") as input_file:
            input_pdf = PdfFileReader(input_file, strict=False)
            watermark = self.__get_orient_watermark_pdf(input_pdf.getPage(0).mediabox)
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
        Storage().remove(self.pdf_file_path)
        Storage().rename(merged, self.pdf_file_path)

    @staticmethod
    def __get_orient_watermark_pdf(input_pdf: RectangleObject) -> str:
        if input_pdf.getUpperRight_x() - input_pdf.getUpperLeft_x() > \
                input_pdf.getUpperRight_y() - input_pdf.getLowerRight_y():
            # print('horizontal')
            return 'ЧЕРНОВИК-HORIZONTAL.pdf'
        else:
            # print('vertical')
            return 'ЧЕРНОВИК-VERTICAL.pdf'
