from tkinter import filedialog as fd
from tkinter import Button, Tk, Label, Checkbutton, BooleanVar
from datetime import datetime
import os
from Code.get_list_of_folders_or_files import (
    get_list_of_folders_names,
    get_list_of_files_names,
)
from Code.copy_folder_or_file import (
    copy_folder,
    copy_file,
)


class Gui:

    title_text = "Копипастер 1.0"

    # Функция выбора пути к папке с исходными данными
    def _choose_folder(self):
        """
        Функция выбора папки в которой хранятся исходные файлы для копирования.
        """
        # Вызываем метод tkinter'а для окна выбора папки.
        self.initial_directory = (
            fd.askdirectory(
                title="Выберите папку",
                initialdir=self.initial_directory)
        )
        # Показываем путь пользователю.
        self._text_folder.configure(text=self.initial_directory)
        # Получаем список папок в папке с исходными данными.
        folders = get_list_of_folders_names(self.initial_directory)
        # переменные в которые записываем результат.
        folders_for_copy = {}
        files_for_copy = {}
        for folder in folders:
            for order in self.orders:
                # Проверяем каждое правило копирования.
                if order.should_be_copied(folder):
                    # Если нужно копировать добавляем пути в список
                    # на копирование для этой папки.
                    paths = order.get_paths(
                        directory=self.initial_directory,
                        name_of_file_or_folder=folder,
                        file_name=folder,
                        )  # метод возвращает лист путей в которые копировать.
                    folders_for_copy[folder] = folders_for_copy.get(folder, [])
                    for path in paths:
                        folders_for_copy[folder].append(path)

        # Получаем список файлов в папке с исходными данными.
        files = get_list_of_files_names(self.initial_directory)
        for file in files:
            for order in self.orders:
                # Проверяем каждое правило копирования.
                if order.should_be_copied(file):
                    # Если нужно копировать добавляем пути в список
                    # на копирование для этой папки.
                    paths = order.get_paths(
                        directory=self.initial_directory,
                        name_of_file_or_folder=file,
                        file_name=file,
                        )  # метод возвращает лист путей в которые копировать.
                    files_for_copy[file] = files_for_copy.get(file, [])
                    for path in paths:
                        files_for_copy[file].append(path)
        # По словарям folders_for_copy и files_for_copy
        # составляем текст с описанием того что будет копировано.
        new_text = ""
        if folders_for_copy:
            new_text += "ПАПКИ, КОТОРЫЕ БУДУТ КОПИРОВАНЫ:\n"
            for k, v in folders_for_copy.items():
                new_text += f"{k}\n"
                for directory in v:
                    new_text += f"путь: {directory}\n"
        if files_for_copy:
            new_text += "ФАЙЛЫ, КОТОРЫЕ БУДУТ КОПИРОВАНЫ:\n"
            for k, v in files_for_copy.items():
                new_text += f"{k}\n"
                for directory in v:
                    new_text += f"путь: {directory}\n"
        # Этот текст демонстрируем пользователю.
        self._text_warning.configure(
            text=new_text,
        )
        # Записываем словари в атрибуты класса.
        self.folders_for_copy = folders_for_copy
        self.files_for_copy = files_for_copy

    def _calculate(self):
        new_text = ""  # Текст описывающий результат копирования.
        # Если есть папки/файлы для копирования,
        # выводим список папок/файлов и список путей в которые копируем.
        if self.folders_for_copy:
            new_text += "ПАПКИ, результат копирования:\n"
        for folder_name, targets in self.folders_for_copy.items():
            new_text += f"{folder_name}\n"
            source = os.path.join(
                os.path.normpath(self.initial_directory),
                folder_name,
            )
            for target in targets:
                try:
                    copy_folder(source, target)
                    new_text += f"{target} - успешно.\n"
                except:
                    new_text += f"{target} - НЕУДАЧНО.\n"
                    raise
        if self.files_for_copy:
            new_text += "ФАЙЛЫ, результат копирования:\n"
        for file_name, targets in self.files_for_copy.items():
            new_text += f"{file_name}\n"
            source = os.path.join(
                os.path.normpath(self.initial_directory),
                file_name,
            )
            for target in targets:
                try:
                    copy_file(source, target)
                    new_text += f"{target} - успешно.\n"
                except:
                    new_text += f"{target} - НЕУДАЧНО.\n"
        # Получившийся текст не должен быть пустым.
        if new_text:
            self._text_warning.configure(
                text=new_text,
            )
        else:
            self._text_warning.configure(
                text="Что-то пошло не так. =\\",
            )

    def __init__(self, orders, initial_directory):
        # Исходная папка
        self.initial_directory = initial_directory
        self.orders = orders
        # Оформление окна
        self._window = Tk()
        self._window.title(self.title_text)
        self._window.geometry("960x600")  # высота подобрана под частный случай.
        # Ширина для кнопок
        width = 20

        # Кнопка выбора папки
        self._folder_selection_button = Button(
                self._window, text="Выбрать папку с исходными файлами",
                width=width * 6 + 12,
                command=self._choose_folder,
                bg="green",
            )
        self._folder_selection_button.grid(
            columnspan=6, column=0, row=0,
            )

        # Текст названия выбранной папки
        self._text_path = (
            Label(text="Название папки"))
        self._text_path.grid(columnspan=6,
                             column=0, row=1)

        # Текст пути к выбранной папке
        self._text_folder = (
            Label(text="Путь к папке"))
        self._text_folder.grid(columnspan=6,
                               column=0, row=2)

        # Кнопка расчета
        self._calculate_button = Button(
            self._window, text="Ctr+C, Ctr+V",
            width=width * 6 + 12,
            command=self._calculate,
            bg="green",
            )
        self._calculate_button.grid(columnspan=6, column=0,
                                    row=3)

        # Текст ошибки
        self._text_warning = (
            Label(text="Копирование еще не выполнялось"))
        self._text_warning.grid(columnspan=6,
                                column=0, row=5)

        # Запускаем окно
        self._window.mainloop()
