import pdf2image


class PdfToJpg:

    def __init__(self, pdf_file_path: str, output_dir: str):
        self.pdf_file_path = pdf_file_path
        self.output_dir = output_dir

    def convert(self):
        images = pdf2image.convert_from_path(self.pdf_file_path)
        print(len(images))
        for i in range(len(images)):
            images[i].save(self.output_dir + 'page' + str(i) + '.jpg', 'JPEG')
