

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


class Order(Матрешка):

    def __init__(self):
        super().__init__()


class RulesForName(Матрешка):

    def __init__(self):
        super().__init__()


class PathsForRule(Матрешка):

    def __init__(self):
        super().__init__()


class FolderForPaths(Матрешка):

    def __init__(self):
        super().__init__()


class Folder:

    def __init__(self):
        self.status = "should be copied"
