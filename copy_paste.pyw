from Code.get_list_of_string_from_file import (
    get_list_of_strings_from_file,
)
from Code.CONSTANTS import (
    FOLDER_WITH_ORDERS,
    INITIAL_DIR,
)
from Code.rule import get_orders
from Code.error_message_box import ErrorGui
from Code.gui import Gui


try:
    # Читаем инструкции: какие файлы куда копировать.
    rules = get_orders(FOLDER_WITH_ORDERS)
    # Читаем стартовую директорию из которой будем начинать выбирать папку
    initial_dir = get_list_of_strings_from_file(
        FOLDER_WITH_ORDERS+"/"+INITIAL_DIR
    )[0]
# Если произошла ошибка, выводим сообщение.
except Exception as error:
    gui = ErrorGui(error.args)
# Если всё в порядке, запускаем окно программы.
else:
    gui = Gui(rules=rules, initial_directory=initial_dir)
