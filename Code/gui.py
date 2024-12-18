import tkinter as tk
from tkinter import filedialog as fd
from tkinter import Button, Tk, Label
from Code.CONSTANTS import (
    FULL_INFO,
    TARGET_FOLDERS,
    # MASKS,
    NAMES_AND_RULES,
    ONLY_NAMES,
)
from Code.get_list_of_folders_or_files import (
    get_list_of_folders_names,
    get_list_of_files_names,
)
from Code.order import spread_order_status
from Code.execute_order import copy_files
from Code.order import Order
from Code.create_order import fill_order
from Code.create_info_list import get_info_list
import os


class Gui:

    title_text = "Копипастер 3.0"

    def _recreate_info_for_user(self):
        self._text_warning.destroy()
        self._text_warning = tk.Listbox(
            width=220, height=29,
            selectmode=tk.MULTIPLE, selectbackground="blue"
        )
        self.info_list = get_info_list(
            mode=self.radiobutton_position.get(),
            order=self.order,
            after_copying=self.after_copying,
        )
        for x in self.info_list:
            self._text_warning.insert(0, x)
        self._text_warning.grid(columnspan=6, column=0, row=5)

    # Функция выбора пути к папке с исходными данными
    def _choose_folder(self):
        # TODO
        # Отработать ситуацию при отказе пользователя от
        # выбора папки.
        self.chosen_directory = (
            fd.askdirectory(
                title="Выберите папку",
                initialdir=self.initial_directory)
        )
        self.after_copying = False
        # Показываем путь пользователю.
        self.project_name = os.path.basename(self.chosen_directory)
        self._text_path.configure(text=self.project_name)
        self._text_folder.configure(text=self.chosen_directory)
        folders = get_list_of_folders_names(self.chosen_directory)
        files = get_list_of_files_names(self.chosen_directory)
        self.order = Order()
        fill_order(
            order=self.order,
            folders=folders, files=files,
            rules=self.rules, source_folder=self.chosen_directory,
            )
        self._recreate_info_for_user()

    def _copy_files(self):
        self.after_copying = True
        copy_files(order=self.order,
                   project_folder=self.project_name,
                   source_folder=self.chosen_directory,)
        spread_order_status(self.order)
        self._recreate_info_for_user()

    def __init__(self, rules,
                 initial_directory, folders_allowed_to_scan):
        # Исходная папка
        self.initial_directory = initial_directory
        self.allowed_folders = folders_allowed_to_scan
        self.chosen_directory = None
        self.rules = rules
        # Оформление окна
        self._window = Tk()
        self._window.title(self.title_text)
        self._window.geometry("1380x600")  # высота подобрана под частный случай.
        # Ширина для кнопок
        width = 30

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
            Label(text="Папка проекта"))
        self._text_path.grid(columnspan=6,
                             column=0, row=1)

        # Текст пути к выбранной папке
        self._text_folder = (
            Label(text="Путь к папке"))
        self._text_folder.grid(columnspan=6,
                               column=0, row=2)

        # Выбор формата вывода информации
        self.radiobutton_position = tk.IntVar(value=4)
        self._radiobutton0 = tk.Radiobutton(
            text="полная информация",
            variable=self.radiobutton_position,
            value=FULL_INFO, command=self._recreate_info_for_user)
        self._radiobutton1 = tk.Radiobutton(
            # TODO
            # добавить вывод выбранных подпапок.
            text="имена файлов, целевые папки",
            variable=self.radiobutton_position,
            value=TARGET_FOLDERS, command=self._recreate_info_for_user)
        # self._radiobutton2 = tk.Radiobutton(
        #     text="псевдонимы, выбранные подпапки (после копирования)",
        #     variable=self.radiobutton_position,
        #     value=MASKS, command=self._recreate_info_for_user)
        self._radiobutton3 = tk.Radiobutton(
            text="имена файлов и правила копирования",
            variable=self.radiobutton_position,
            value=NAMES_AND_RULES, command=self._recreate_info_for_user)
        self._radiobutton4 = tk.Radiobutton(
            text="только имена файлов",
            variable=self.radiobutton_position,
            value=ONLY_NAMES, command=self._recreate_info_for_user)
        self._radiobutton0.grid(column=0, row=3)
        self._radiobutton1.grid(column=1, row=3)
        # self._radiobutton2.grid(column=2, row=3)
        self._radiobutton3.grid(column=3, row=3)
        self._radiobutton4.grid(column=4, row=3)

        # Кнопка расчета
        self._calculate_button = Button(
            self._window, text="Ctr+C, Ctr+V",
            width=width * 6 + 12,
            command=self._copy_files,
            bg="green",
            )
        self._calculate_button.grid(columnspan=6, column=0,
                                    row=4)

        # Текст ошибки

        self._text_warning = tk.Label(text="Не выбрана папка исходных данных")
        self._text_warning.grid(columnspan=6, column=0, row=5)

        # Запускаем окно
        self._window.mainloop()
