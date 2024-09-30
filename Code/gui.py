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
        Функция выбора папки в которую будет выводиться файл с выполненными
        расчетами.
        """
        self.initial_directory = (
            fd.askdirectory(
                title="Выберите папку",
                initialdir=self.initial_directory)
        )
        self._text_folder.configure(text=self.initial_directory)
        folders = get_list_of_folders_names(self.initial_directory)
        folders_for_copy = {}
        files_for_copy = {}
        for folder in folders:
            for order in self.orders:
                if order.should_be_copied(folder):
                    paths = order.get_paths(
                        directory=self.initial_directory,
                        name_of_file_or_folder=folder,
                        into_folder_with_same_name=self.in_same_folder.get(),
                        file_name=folder,
                        )
                    folders_for_copy[folder] = folders_for_copy.get(folder, [])
                    for path in paths:
                        folders_for_copy[folder].append(path)
                    
        files = get_list_of_files_names(self.initial_directory)
        for file in files:
            for order in self.orders:
                if order.should_be_copied(file):
                    paths = order.get_paths(
                        directory=self.initial_directory,
                        name_of_file_or_folder=file,
                        into_folder_with_same_name=self.in_same_folder.get(),
                        file_name=file,
                        )
                    files_for_copy[file] = files_for_copy.get(file, [])
                    for path in paths:
                        files_for_copy[file].append(path)
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
        self._text_warning.configure(
            text=new_text,
        )
        self.folders_for_copy = folders_for_copy
        self.files_for_copy = files_for_copy


    def _calculate(self):
        new_text = ""
        if not self.in_same_folder.get():
            self._text_warning.configure(
                text="Копировать в общую папку проектов нельзя."
                )
            return
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
        self._window.geometry("960x300")
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

        # Условия
        self.in_same_folder = BooleanVar(value=True)

        self._checkbutton = Checkbutton(
            self._window, text="В папке с тем же названием",
            variable=self.in_same_folder,
            onvalue=True, offvalue=False,
        )
        self._checkbutton.grid(column=0, row=4)

        # Текст ошибки
        self._text_warning = (
            Label(text="Копирование еще не выполнялось"))
        self._text_warning.grid(columnspan=6,
                                column=0, row=5)

        # Запускаем окно
        self._window.mainloop()
