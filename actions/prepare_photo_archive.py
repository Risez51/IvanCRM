"""
    Designed to create an archive with folders that contain photos.
    Accepts a directory with folders whose names are equal to the article.
    It sorts through the article in the first column in .csv, .xls, .xlsx files
    (the file with the article upload without a photo),
    looks for the article that matches the name of the folder with the article and moves it to the resulting directory
 """

from file_manager.storage import Storage


class PreparePhotoArchive(Storage):
    def __init__(self, dir_with_photo_path: str, file_with_articles_path: str, result_dir_path: str):
        super().__init__()
        self.__dir_with_photo_path = dir_with_photo_path
        self.__file_with_articles_path = file_with_articles_path
        self.__result_dir_path = result_dir_path

    def start(self):
        articles_list_without_photo = self.get_data_from_excel(self.__file_with_articles_path)
        dirs_list_with_photo = self.get_filenames(self.__dir_with_photo_path)

        for row in articles_list_without_photo:
            article = str(row[0])
            self.__find_folder_by_name(dirs_list_with_photo, article)

    def __find_folder_by_name(self, dir_for_find: list, search_folder_name: str):
        for current_folder_name in dir_for_find:
            if str(current_folder_name) == search_folder_name:
                self.move(self.__dir_with_photo_path, self.__result_dir_path, current_folder_name)
                break
