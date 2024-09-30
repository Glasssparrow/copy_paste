from tkinter import filedialog as fd
from tkinter import Button, Tk, Label, Checkbutton, BooleanVar
from datetime import datetime


class Gui:

    title_text = "Копипастер 1.0"

    # Функция нужна для формирования пути к папке из пути к файлу.
    @staticmethod
    def _cut_filename(path_to_file):
        """
        Обрабатывает путь к файлу в формате - ххх/ххх/file.file.
        Отсекает часть /file.file оставляя ххх/ххх
        """
        split = path_to_file.split("/")
        # Получаем длину последнего фрагмента после "/".
        # Прибавляем единицу т.к. "/" тоже убираем.
        delete = len(split[len(split)-1])+1
        return path_to_file[:-delete]


    # Функция выбора пути к папке с исходными данными
    def _choose_folder(self):
        """
        Функция выбора папки в которую будет выводиться файл с выполненными
        расчетами.
        """
        self.output_path = (
            fd.askdirectory(title="Выберите папку",
                            initialdir=self.output_path)
        )
        self._text_folder.configure(text=self.output_path)


    def _calculate(self):
        pass


    def __init__(self):
        # Оформление окна
        self._window = Tk()
        self._window.title(self.title_text)
        self._window.geometry("500x200")
        # Ширина для кнопок
        width = 12


        # Кнопка выбора папки
        self._folder_selection_button = (
            Button(self._window, text="Выбрать папку для печати",
                   width=width * 2 + 2,
                   command=self._choose_folder)
        )
        self._folder_selection_button.grid(
            columnspan=2, column=0, row=0
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
            self._window, text="Рассчитать",
            width=width * 6 + 6,
            command=self._calculate,
            bg="green"
            )
        self._calculate_button.grid(columnspan=6, column=0,
                                    row=3)

        self.allow_nodes_without_quantity = BooleanVar(value=True)

        self._checkbutton = Checkbutton(
            self._window, text="доп. узлы",
            variable=self.allow_nodes_without_quantity,
            onvalue=True, offvalue=False,
        )
        self._checkbutton.grid(column=0, row=4)

        # Текст ошибки
        self._text_warning = (
            Label(text="Расчет еще не выполнялся"))
        self._text_warning.grid(columnspan=6,
                                column=0, row=5)

        # Запускаем окно
        self._window.mainloop()
