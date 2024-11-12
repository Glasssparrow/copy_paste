from Code.CONSTANTS import (
    SHOULD_BE_COPIED,
    SHOULD_BE_COPIED_PARTIALLY,
    SHOULD_NOT_BE_COPIED,
    SUCCESFUL,
    PARTIALLY_SUCCESFUL,
    NOT_SUCCESFUL,
    WASNT_COPIED,
    WAS_COPIED,
)

# Класс должен содержать всю необходимую информацию для копирования.
# Класс должен содержать всю необходимую информацию о результатах копирования.


class Матрешка:

    def __init__(self):
        self.data = []
        self.status = SHOULD_BE_COPIED

    def ask_status(self):
        succesful = 0
        not_succesful = 0
        first_iteration = True
        was_copied = None
        for element in data:
            if first_iteration:
                if element.status in WAS_COPIED:
                    was_copied = True
                else:
                    was_copied = False
            if element.status in YES:
                succesful += 1
            else:
                not_succesful += 1
            if (
                not first_iteration and
                ((was_copied and element.status in WASNT_COPIED) or
                 (not was_copied and element.status in WAS_COPIED))
            ):
                raise Exception(
                    f"Часть файлов помечена как результат"
                    "а часть как задание на копирование"
                )
            first_iteration = False
        done = self._how_much_done(succesful, not_succesful)
        if was_copied:
            if done == 0:
                self.status = NOT_SUCCESFUL
            elif done == 0.5:
                self.status = PARTIALLY_SUCCESFUL
            elif done == 1:
                self.status = SUCCESFUL
        else:
            if done == 0:
                self.status = SHOULD_NOT_BE_COPIED
            elif done == 0.5:
                self.status = SHOULD_BE_COPIED_PARTIALLY
            elif done == 1:
                self.status = SHOULD_BE_COPIED

    def _how_much_done(done, not_done):
        if (done + not_done) <= 0:
            raise Exception("something went wrong")
        if not_done == 0:
            return 1
        elif done == 0:
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
