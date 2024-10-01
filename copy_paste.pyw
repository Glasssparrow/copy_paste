from Code.get_list_of_folders_or_files import (
    get_list_of_folders_names,
    get_list_of_files_names,
)
from Code.get_list_of_string_from_file import (
    get_list_of_strings_from_file,
)
from Code.order import get_orders
from Code.error_message_box import ErrorGui
from Code.gui import Gui


try:
    orders = get_orders("Data")
    initial_dir = get_list_of_strings_from_file("Data/initial_dir.txt")[0]
except Exception as error:
    gui = ErrorGui(error.args)
else:
    gui = Gui(orders=orders, initial_directory=initial_dir)