"""
    Class for convert .pdf file to .jpg file/s.
    pdf_file_path = current path to pdf file, ends with file.pdf
    output_dir = directory for save jpg file
"""

import pdf2image


class PdfToJpg:
    def __init__(self, pdf_file_path: str, output_dir: str):
        self.pdf_file_path = pdf_file_path
        self.output_dir = output_dir

    def convert(self):
        images = pdf2image.convert_from_path(self.pdf_file_path)
        for i in range(len(images)):
            images[i].save(self.output_dir + '\\' + str(i) + '.jpg', 'JPEG')
