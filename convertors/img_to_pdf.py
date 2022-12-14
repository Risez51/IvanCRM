"""
    Converts one or more .jpg files into one .pdf file.
"""

from PIL import Image
from file_manager.storage import Storage


class ImgToPdf:
    def __init__(self, dir_with_img_files: str, path_to_save: str):
        self.dir_with_img_files = dir_with_img_files
        self.path_to_save = path_to_save

    def convert(self, pdf_result_name: str):
        image_list = Storage().get_filenames(self.dir_with_img_files)
        img_files = [Image.open(self.dir_with_img_files + '\\' + img) for img in image_list]
        img_files[0].save(f'{self.path_to_save}\\{pdf_result_name}', save_all=True, append_images=img_files[1:])
