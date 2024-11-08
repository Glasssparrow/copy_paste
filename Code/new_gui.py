import tkinter as tk
from tkinter import filedialog as fd
from tkinter import Button, Tk, Label, Frame, StringVar, Entry, Scrollbar
import os


class Gui:

    title_text = "Копипастер 3.0"

    def _recreate_info_for_user(self):
        self._text_warning.destroy()
        self._text_warning = tk.Label(text=str(self.radionbutton_position.get()))
        self._text_warning.grid(columnspan=6, column=0, row=5)

    # Функция выбора пути к папке с исходными данными
    def _choose_folder(self):
        self._text_warning.destroy()
        self._text_warning = tk.Listbox(width=220, height=29,)
        for x in range(100):
            self._text_warning.insert(0, "Копирование не выполнялось"+str(x))
        self._text_warning.grid(columnspan=6, column=0, row=5)

    def _copy_files(self):
        pass

    def __init__(self):
        # Исходная папка
        self.initial_directory = "test"
        self.orders = None
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
        self.radionbutton_position = tk.IntVar(value=2)
        self._radiobutton0 = tk.Radiobutton(
            text="полная информация",
            variable=self.radionbutton_position, value=0, command=self._recreate_info_for_user)
        self._radiobutton1 = tk.Radiobutton(
            text="только полные пути копирования",
            variable=self.radionbutton_position, value=1, command=self._recreate_info_for_user)
        self._radiobutton2 = tk.Radiobutton(
            text="целевые папки, выбранные подпапки (после копирования)",
            variable=self.radionbutton_position, value=2, command=self._recreate_info_for_user)
        self._radiobutton3 = tk.Radiobutton(
            text="псевдонимы, выбранные подпапки (после копирования)",
            variable=self.radionbutton_position, value=3, command=self._recreate_info_for_user)
        self._radiobutton4 = tk.Radiobutton(
            text="только имена файлов",
            variable=self.radionbutton_position, value=4, command=self._recreate_info_for_user)
        self._radiobutton0.grid(column=0, row=3)
        self._radiobutton1.grid(column=1, row=3)
        self._radiobutton2.grid(column=2, row=3)
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


gui = Gui()
