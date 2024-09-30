from Code.get_list_of_folders_or_files import (
    get_list_of_folders_names
)
from Code.order import get_orders
from Code.error_message_box import ErrorGui
from Code.gui import Gui


try:
    orders = get_orders("Data")
except Exception as error:
    gui = ErrorGui(error.args)
else:
    gui = Gui()
