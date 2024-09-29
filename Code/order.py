from Code.get_list_of_folders_or_files import (
    get_list_of_folders_names,
    get_list_of_files_names,
)
from Code.get_list_of_string_from_file import get_list_of_strings_from_file


class Order:

    def __init__(self):
        pass


def get_orders():
    folders_with_orders = get_list_of_folders_names("Data")
