from Code.get_list_of_folders_or_files import (
    get_list_of_folders_names,
    get_list_of_files_names,
)
from Code.get_list_of_string_from_file import (
    get_list_of_strings_from_file,
)
from Code.CONSTANTS import (
    TARGET_DIRECTORIES_STORAGE,
    FILE_EXTENSIONS_STORAGE,
    LAST_PARTS_OF_NAMES_STORAGE,
)
import os


class Order:

    def __init__(self):
        pass


def get_orders(relative_path):
    folders_with_orders = get_list_of_folders_names(relative_path)
    for folder in folders_with_orders:
        path = os.path.join(relative_path, folder)
        files = get_list_of_files_names(path)
        # Проверяем что есть все нужные файлы.
        # Создаем экземпляр класса Order.
        # Если чего-то не хватает - поднимаем ошибку.
        # Текст ошибки содержит описание проблемы.
        if (
                TARGET_DIRECTORIES_STORAGE in files and
                FILE_EXTENSIONS_STORAGE in files and
                LAST_PARTS_OF_NAMES_STORAGE in files
        ):
            order = Order()
        else:
            files_not_found = []
            if TARGET_DIRECTORIES_STORAGE not in files:
                files_not_found.append(TARGET_DIRECTORIES_STORAGE)
            if FILE_EXTENSIONS_STORAGE not in files:
                files_not_found.append(FILE_EXTENSIONS_STORAGE)
            if LAST_PARTS_OF_NAMES_STORAGE not in files:
                files_not_found.append(LAST_PARTS_OF_NAMES_STORAGE)
            raise Exception(
                f"Не хватает файлов {files_not_found} в папке {folder}."
            )
        # Записываем в order пути куда копировать.
        target_directories_path = os.path.join(
            relative_path,
            folder,
            TARGET_DIRECTORIES_STORAGE,
        )
        text_list = get_list_of_strings_from_file(target_directories_path)
        # Записываем в order допустимые расширения.
        file_extensions_path = os.path.join(
            relative_path,
            folder,
            FILE_EXTENSIONS_STORAGE,
        )
        text_list = get_list_of_strings_from_file(file_extensions_path)
        # Записываем в order допустимые окончания имен.
        for_names_path = os.path.join(
            relative_path,
            folder,
            LAST_PARTS_OF_NAMES_STORAGE,
        )
        text_list = get_list_of_strings_from_file(for_names_path)
