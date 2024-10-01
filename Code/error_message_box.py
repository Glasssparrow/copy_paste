from tkinter import Button, Tk, Label, Checkbutton, BooleanVar
from datetime import datetime


class ErrorGui:

    title_text = "Error message box"

    def __init__(self, message_tuple):
        # Оформление окна
        self._window = Tk()
        self._window.title(self.title_text)
        self._window.geometry("500x100")
        # Записываем данные об ошибке из исключения.
        self.message_text = ""
        for tuple_element in message_tuple:
            self.message_text += tuple_element


        # Сообщение об ошибке
        self._text_path = Label(text=self.message_text)
        self._text_path.grid(column=0, row=0)
        # Запускаем окно
        self._window.mainloop()
