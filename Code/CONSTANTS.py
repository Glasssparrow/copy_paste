

# Файл с начальным путем для выбора папки
INITIAL_DIR = "начальная_директория.txt"
# Файл со списком папок в которых можно искать файлы
SOURCE_FOLDERS = "ищем_в_папках.txt"
# Папка с правилами копирования
FOLDER_WITH_ORDERS = "Правила копирования"

# Файл содержащий пути к папкам проектов, в которые копируем.
TARGET_DIRECTORIES_STORAGE = "пути к папкам проектов.txt"
# Файл содержащий подпапки внутри папки проекта, в которые будем копировать.
TARGET_FOLDER_STORAGE = "варианты целевых папок в папках проекта.txt"

# Файл содержащий расширения файлов, которые будем копировать.
FILE_EXTENSIONS_STORAGE = "допустимые расширения.txt"
# Файл содержащий начала имен файлов, которые будем копировать.
FIRST_PARTS_OF_NAMES_STORAGE = "допустимые начала имен.txt"
# Файл содержащий окончания имен файлов, которые будем копировать.
LAST_PARTS_OF_NAMES_STORAGE = "допустимые окончания имен.txt"

# Файл содержащий полные имена файлов, которые будем копировать.
FULL_NAMES_STORAGE = "список файлов для копирования.txt"

# Метка разрешения копирования папок в FILE_EXTENSIONS_STORAGE
CAN_COPY_FOLDERS = "папка"


# Статусы копирования
SHOULD_BE_COPIED = "SHOULD_BE_COPIED"
SHOULD_BE_COPIED_PARTIALLY = "SHOULD_BE_COPIED_PARTIALLY"
SHOULD_NOT_BE_COPIED = "SHOULD_NOT_BE_COPIED"

WASNT_COPIED = [SHOULD_BE_COPIED, SHOULD_BE_COPIED_PARTIALLY, SHOULD_NOT_BE_COPIED]

SUCCESSFUL = "успешно"
PARTIALLY_SUCCESSFUL = "ЧАСТЬ НЕ СКОПИРОВАНА"
NOT_SUCCESSFUL = "НЕУДАЧНО"

WAS_COPIED = [SUCCESSFUL, PARTIALLY_SUCCESSFUL, NOT_SUCCESSFUL]

YES = [SUCCESSFUL, SHOULD_BE_COPIED]

FULL_INFO = 0
TARGET_FOLDERS = 1
MASKS = 2
NAMES_AND_RULES = 3
ONLY_NAMES = 4

