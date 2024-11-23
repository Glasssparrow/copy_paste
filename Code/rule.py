from Code.get_list_of_folders_or_files import (
    get_list_of_folders_names,
    get_list_of_files_names,
)
from Code.get_list_of_string_from_file import (
    get_list_of_strings_from_file,
)
from Code.CONSTANTS import (
    FULL_NAMES_STORAGE,
    TARGET_DIRECTORIES_STORAGE,
    TARGET_FOLDER_STORAGE,
    FILE_EXTENSIONS_STORAGE,
    FIRST_PARTS_OF_NAMES_STORAGE,
    LAST_PARTS_OF_NAMES_STORAGE,
    CAN_COPY_FOLDERS,
)
import os


class Rule:

    def __init__(self, name: str):
        self.name = name  # Имя правила

        self.target = None  # Пути к папкам проектов
        self.folders_options = None  # Папки в папках проекта.

        self.can_copy_folders = False

        # Для случая, когда self.only_full_names == False
        self.extensions = None  # Расширения
        self.firsts_parts = None  # Начала имен
        self.last_parts = None  # Окончания имен

    def should_be_copied(self, name_with_extension, is_folder: bool, full_path=False):
        if is_folder and not self.can_copy_folders:
            return False
        # Если получили полный путь, то отделяем имя.
        if full_path:
            name_with_extension = os.path.basename(
                name_with_extension)
        # Если ограничений совсем нет, то что-то не так.
        if (
            not self.firsts_parts and
            not self.last_parts and
            (not self.extensions and not self.can_copy_folders)
        ):
            raise Exception(
                f"Не найдены правила для {self.name}"
            )
        # Проверяем проходит ли расширение
        extension_fit = False
        for extension in self.extensions:
            # Расширение должно совпадать с
            # правилом на копирование.
            file_extension = os.path.splitext(name_with_extension)[1]
            if file_extension == extension:
                extension_fit = True
        # Проверяем проходит ли имя
        last_part_of_name_fit = False
        for name_requirement in self.last_parts:
            # Окончание имени должно совпадать с
            # правилом на копирование.
            if not is_folder:
                file_name = os.path.splitext(name_with_extension)[0]
            else:
                file_name = name_with_extension
            if file_name[-len(name_requirement):] == name_requirement:
                last_part_of_name_fit = True
        first_part_of_name_fit = False
        for name_requirement in self.firsts_parts:
            # Начало имени должно совпадать с
            # правилом на копирование.
            if not is_folder:
                file_name = os.path.splitext(name_with_extension)[0]
            else:
                file_name = name_with_extension
            if file_name[:len(name_requirement)] == name_requirement:
                first_part_of_name_fit = True

        # Если все три условия выполняются или отсутствуют, то
        # возвращаем True.
        if not self.firsts_parts or first_part_of_name_fit:
            if not self.last_parts or last_part_of_name_fit:
                if not self.extensions or extension_fit or is_folder:
                    return True
        return False

    @staticmethod
    def create_path(
        main_directory,
        last_folder,
        additional_directory,
        file_name,
    ):
        # Собираем вместе
        # папка_куда_копировать/папка_проекта/доп_папки/назв_файла
        path = os.path.join(
            main_directory,
            last_folder,
            additional_directory,
            file_name,
        )
        return path

    def get_paths(
            self,
            directory: str,  # Папка из которой копируем.
            is_folder_and_not_a_file: bool,
            name_of_file_or_folder: str,
            ):
        # normpath - нормализует путь (убирает / в конце если он есть).
        # / может сломать basename.
        # basename возвращает последнюю часть пути.
        source_folder = os.path.basename(os.path.normpath(
            directory,
            ))
        paths = []
        # Проходим по целевым папкам для копирования
        for main_directory in self.target:
            if not self.folders_options:
                # Если подпапок нет
                path = self.create_path(
                    main_directory=main_directory,
                    last_folder=source_folder,
                    additional_directory="",
                    file_name=name_of_file_or_folder,
                )
                paths.append(path)
            # Каждой подпапке по пути.
            for additional_directory in self.folders_options:
                path = self.create_path(
                    main_directory=main_directory,
                    last_folder=source_folder,
                    additional_directory=additional_directory,
                    file_name=name_of_file_or_folder,
                )
                paths.append(path)
        return paths


def get_orders(relative_path):
    # Получаем список папок с правилами для копирования.
    folders_with_orders = get_list_of_folders_names(relative_path)
    orders = []  # Списов приказов на копирование.
    # Проходим по всем папкам с правилами для копирования.
    for folder in folders_with_orders:
        path = os.path.join(relative_path, folder)
        files = get_list_of_files_names(path)
        # Проверяем что есть все нужные файлы.
        # Создаем экземпляр класса Order.
        # Если чего-то не хватает - поднимаем ошибку.
        # Текст ошибки содержит описание проблемы.
        if (
                FILE_EXTENSIONS_STORAGE in files and
                FIRST_PARTS_OF_NAMES_STORAGE in files and
                LAST_PARTS_OF_NAMES_STORAGE in files and
                FULL_NAMES_STORAGE in files
        ):
            raise Exception(
                f"В папке {folder} найден и список полных имен файлов "
                f"и правила фильтрации имен. Должно быть что-то одно."
            )
        elif (
                TARGET_DIRECTORIES_STORAGE in files and
                TARGET_FOLDER_STORAGE in files and
                FILE_EXTENSIONS_STORAGE in files and
                FIRST_PARTS_OF_NAMES_STORAGE in files and
                LAST_PARTS_OF_NAMES_STORAGE in files
        ):
            rule = Rule(name=folder)
            orders.append(rule)
        else:
            # Если что-то не нашли в правиле - исключение.
            files_not_found = []
            if TARGET_DIRECTORIES_STORAGE not in files:
                files_not_found.append(TARGET_DIRECTORIES_STORAGE)
            if TARGET_FOLDER_STORAGE not in files:
                files_not_found.append(TARGET_FOLDER_STORAGE)
            if FILE_EXTENSIONS_STORAGE not in files:
                files_not_found.append(FILE_EXTENSIONS_STORAGE)
            if FIRST_PARTS_OF_NAMES_STORAGE not in files:
                files_not_found.append(FIRST_PARTS_OF_NAMES_STORAGE)
            if LAST_PARTS_OF_NAMES_STORAGE not in files:
                files_not_found.append(LAST_PARTS_OF_NAMES_STORAGE)
            raise Exception(
                f"Не хватает файлов {files_not_found} в папке {folder}."
            )
        # Записываем в rule пути куда копировать.
        target_directories_path = os.path.join(
            relative_path,
            folder,
            TARGET_DIRECTORIES_STORAGE,
        )
        text_list = get_list_of_strings_from_file(target_directories_path)
        rule.target = text_list
        target_folder = os.path.join(
            relative_path,
            folder,
            TARGET_FOLDER_STORAGE,
        )
        text_list = get_list_of_strings_from_file(target_folder)
        rule.folders_options = text_list

        # Формируем правила для выбора файлов.
        # Записываем в rule допустимые расширения.
        file_extensions_path = os.path.join(
            relative_path,
            folder,
            FILE_EXTENSIONS_STORAGE,
        )
        text_list = get_list_of_strings_from_file(file_extensions_path)
        number = None
        for n, line in enumerate(text_list):
            if line == CAN_COPY_FOLDERS:
                number = n
        if number is not None:
            text_list.pop(number)
            rule.can_copy_folders = True

        rule.extensions = text_list
        # Записываем в rule допустимые начала имен.
        for_names_path = os.path.join(
            relative_path,
            folder,
            FIRST_PARTS_OF_NAMES_STORAGE,
        )
        text_list = get_list_of_strings_from_file(for_names_path)
        rule.firsts_parts = text_list
        # Записываем в rule допустимые окончания имен.
        for_names_path = os.path.join(
            relative_path,
            folder,
            LAST_PARTS_OF_NAMES_STORAGE,
        )
        text_list = get_list_of_strings_from_file(for_names_path)
        rule.last_parts = text_list
    return orders
