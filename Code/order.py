from Code.get_list_of_folders_or_files import (
    get_list_of_folders_names,
    get_list_of_files_names,
)
from Code.get_list_of_string_from_file import (
    get_list_of_strings_from_file,
)
from CONSTANTS import (
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
        for file_name in files:
            path_to_file = os.path.join(
                relative_path,
                folder,
                file_name,
            )
            text_list = get_list_of_strings_from_file(path_to_file)
