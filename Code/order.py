

# Создать класс команды на копирование.
# Order переименовать в Rule во избежание путаницы.

# Класс должен содержать всю необходимую информацию для копирования.
# Класс должен содержать всю необходимую информацию о результатах копирования.

# Учесть что класс должен содержать информацию о том на какие папки
# поступал приказ копировать (они были выделены), а на какие - нет.


class Матрешка:

    def __init__(self):
        self.data = []
        self.status = "should be copied"

    def set_status(self, status):
        self.status = status
        for element in self.data:
            element.set_status(status)

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, item):
        pass

    def append(self, item):
        pass


# Полный приказ на копирование.
class Order(Матрешка):

    def __init__(self):
        super().__init__()


# Правила для отдельного файла (или папки)
class RulesForName(Матрешка):

    def __init__(self, is_folder: bool):
        super().__init__()
        self.is_folder = is_folder


# Пути копирования для отдельного файла.
class PathsForRule(Матрешка):

    def __init__(self):
        super().__init__()


# Подпапки для каждого пути.
class FolderForPaths(Матрешка):

    def __init__(self):
        super().__init__()


# Отдельная подпапка.
class Folder:

    def __init__(self):
        self.status = "should be copied"
