import tkinter as tk
from tkinter import filedialog as fd
from tkinter import Button, Tk, Label, Frame, StringVar, Entry, Scrollbar
import os


class Gui:

    title_text = "Копипастер 2.0"

    # Функция выбора пути к папке с исходными данными
    def _choose_folder(self):
        """
        Функция выбора папки в которой хранятся исходные файлы для копирования.
        """
        pass

    def _copy_files(self):
        pass

    def __init__(self):
        # Исходная папка
        self.initial_directory = "test"
        self.orders = None
        # Оформление окна
        self._window = Tk()
        self._window.title(self.title_text)
        self._window.geometry("1450x600")  # высота подобрана под частный случай.
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
            command=self._copy_files,
            bg="green",
            )
        self._calculate_button.grid(columnspan=6, column=0,
                                    row=3)

        # Текст ошибки

        root = self._window
        def on_configure(event):
            # update scrollregion after starting 'mainloop'
            # when all widgets are in canvas
            canvas.configure(scrollregion=canvas.bbox('all'))
    
        # --- create canvas with scrollbar ---

        canvas = tk.Canvas(root, width=1200, height=500)
        canvas.grid()

        scrollbar = tk.Scrollbar(root, command=canvas.yview)
        scrollbar.grid(column=6, row=4, rowspan=2)

        canvas.configure(yscrollcommand = scrollbar.set)

        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        canvas.bind('<Configure>', on_configure)

        # --- put frame in canvas ---

        self.frame = tk.Frame(canvas)
        canvas.create_window((0,0), window=self.frame, anchor='nw')

        # --- add widgets in frame ---

        self._text_warning = tk.Label(self.frame, text=" "*190+"Копирование не выполнялось"+"\n"*100,
                                      justify="left")
        self._text_warning.grid(columnspan=6, column=0, row=4, rowspan=2)

        # Запускаем окно
        self._window.mainloop()


gui = Gui()
