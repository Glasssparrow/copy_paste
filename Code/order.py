

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

    def ask_status(self):
        succesful = 0
        not_succesful = 0
        for element in data:
            if element.status == "SUCCESFUL":
                succesful += 1
            else:
                not_succesful += 1

    def _choose_status(done, not_done):
        if (done + not_done) <= 0:
            raise Exception("something went wrong")
        if not_done = 0:
            return 1
        elif done = 0:
            return 0
        else:
            return 0.5
        

    def _validate_key(key):
        if not isinstance(key, int):
            raise Exception(
                f"{key} должно быть целым числом (int)"
            )
        if key >= len(self.data):
            raise Exception(
                f"{key} >= количества данных"
            )

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
