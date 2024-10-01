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
    TARGET_FOLDER_STORAGE,
)
import os


class Order:

    def __init__(self, name):
        self.name = name
        self.target = None
        self.names = None
        self.extensions = None
        self.target_folder = None

    def should_be_copied(self, name_with_extension, full_path=False):
        if full_path:
            name_with_extension = os.path.basename(
                name_with_extension)
        # Если ограничений совсем нет, то что-то не так.
        if (
            not self.names and
            not self.extensions
        ):
            raise Exception(
                f"Не найдены правила для {self.name}"
            )
        # Проверяем проходит ли расширение
        extension_fit = False
        for extension in self.extensions:
            file_extension = os.path.splitext(name_with_extension)[1]
            if file_extension == extension:
                extension_fit = True
        # Проверяем проходит ли имя
        name_fit = False
        for name_requirement in self.names:
            file_name = os.path.splitext(name_with_extension)[0]
            if file_name[-len(name_requirement):] == name_requirement:
                name_fit = True

        # Если оба условия выполняются или отсутствуют, то
        # возвращаем True.
        if not self.names or name_fit:
            if not self.extensions or extension_fit:
                return True
        return False


    @staticmethod
    def create_path(
        main_directory,
        last_folder,
        additional_directory,
        file_name,
    ):
        path = os.path.join(
            main_directory,
            last_folder,
            additional_directory,
            file_name,
        )
        return path

    def get_paths(
            self,
            directory,
            name_of_file_or_folder,
            file_name,
        ):
        # normpath - нормализует путь (убирает / в конце если он есть).
        # / может сломать basename.
        # basename возвращает последнюю часть пути.
        last_folder = os.path.basename(os.path.normpath(
            directory,
            ))
        paths = []
        for main_directory in self.target:
            if not self.target_folder:
                path = self.create_path(
                    main_directory=main_directory,
                    last_folder=last_folder,
                    additional_directory="",
                    file_name=file_name,
                )
                paths.append(path)
            for additional_directory in self.target_folder:
                path = self.create_path(
                    main_directory=main_directory,
                    last_folder=last_folder,
                    additional_directory=additional_directory,
                    file_name=file_name,
                )
                paths.append(path)
        return paths


def get_orders(relative_path):
    folders_with_orders = get_list_of_folders_names(relative_path)
    orders = []
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
                LAST_PARTS_OF_NAMES_STORAGE in files and
                TARGET_FOLDER_STORAGE in files
        ):
            order = Order(folder)
            orders.append(order)
        else:
            files_not_found = []
            if TARGET_DIRECTORIES_STORAGE not in files:
                files_not_found.append(TARGET_DIRECTORIES_STORAGE)
            if FILE_EXTENSIONS_STORAGE not in files:
                files_not_found.append(FILE_EXTENSIONS_STORAGE)
            if LAST_PARTS_OF_NAMES_STORAGE not in files:
                files_not_found.append(LAST_PARTS_OF_NAMES_STORAGE)
            if TARGET_FOLDER_STORAGE not in files:
                files_not_found.append(TARGET_FOLDER_STORAGE)
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
        order.target = text_list
        target_folder = os.path.join(
            relative_path,
            folder,
            TARGET_FOLDER_STORAGE,
        )
        text_list = get_list_of_strings_from_file(target_folder)
        order.target_folder = text_list
        # Записываем в order допустимые расширения.
        file_extensions_path = os.path.join(
            relative_path,
            folder,
            FILE_EXTENSIONS_STORAGE,
        )
        text_list = get_list_of_strings_from_file(file_extensions_path)
        order.extensions = text_list
        # Записываем в order допустимые окончания имен.
        for_names_path = os.path.join(
            relative_path,
            folder,
            LAST_PARTS_OF_NAMES_STORAGE,
        )
        text_list = get_list_of_strings_from_file(for_names_path)
        order.names = text_list
    return orders
