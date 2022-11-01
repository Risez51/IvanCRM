from PIL import Image
from storage import Storage


class ImgToPdf:
    def __init__(self, dil_with_img_files: str, path_to_save: str, pdf_result_name: str):
        self.dir_with_img_files = dil_with_img_files
        self.pdf_result_name = pdf_result_name
        self.path_to_save = path_to_save

    def convert(self):
        # print(f'Преобразование JPG в PDF: {self.pdf_result_name}')
        image_list = Storage().get_files_name(self.dir_with_img_files)
        img_files = [Image.open(self.dir_with_img_files + '\\' + img) for img in image_list]
        img_files[0].save(f'{self.path_to_save}\\{self.pdf_result_name}', save_all=True, append_images=img_files[1:])
