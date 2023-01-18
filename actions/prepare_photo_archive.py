"""
    Designed to create an archive with folders that contain photos.
    Accepts a directory with folders whose names are equal to the article.
    It sorts through the article in the first column in .csv, .xls, .xlsx files
    (the file with the article upload without a photo),
    looks for the article that matches the name of the folder with the article and moves it to the resulting directory
 """

from file_manager.storage import Storage


class PreparePhotoArchive:

    def __init__(self, photo_archive_location: str, result_dir_path: str):
        self.__photo_archive_location = photo_archive_location
        self.__result_dir_path = result_dir_path

    def start_one(self, article: str):
        Storage().move(self.__photo_archive_location, self.__result_dir_path, article)

