import pdf2image
from storage import Storage

class PdfToJpg(Storage):

    def __init__(self, pdf_file_path: str, output_dir: str):
        self.pdf_file_path = pdf_file_path
        self.output_dir = output_dir

    def convert(self):
        template_folder = self.output_dir + '\\template'
        self.create_folder(template_folder)
        images = pdf2image.convert_from_path(self.pdf_file_path)
        print(len(images))
        for i in range(len(images)):
            images[i].save(template_folder + '\\' + 'page-' + str(i) + '.jpg', 'JPEG')
