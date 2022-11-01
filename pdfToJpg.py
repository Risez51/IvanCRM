import pdf2image
from storage import Storage


class PdfToJpg(Storage):
    def __init__(self, pdf_file_path: str, output_dir: str):
        self.pdf_file_path = pdf_file_path
        self.output_dir = output_dir

    def convert(self):
        # print(f'Преобразование в JPG: {self.get_file_name(self.pdf_file_path)}')
        images = pdf2image.convert_from_path(self.pdf_file_path)
        for i in range(len(images)):
            images[i].save(self.output_dir + '\\' + str(i) + '.jpg', 'JPEG')
