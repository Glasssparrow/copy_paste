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
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, item):
        self.data.pop(item)

    def append(self, item):
        self.data.append(item)


# Полный приказ на копирование. Содержит правила.
class Order(Матрешка):

    def __init__(self):
        super().__init__()


# Отдельный файл(или папка). Содержит правила подходящие для него.
class RulesForName(Матрешка):

    def __init__(self, is_folder: bool, name: str):
        super().__init__()
        self.name = name
        self.is_folder = is_folder


# Отдельное правило для копирования. Содержит пути копирования.
class PathsForRule(Матрешка):

    def __init__(self, rule):
        super().__init__()
        self.rule = rule


# Отделный путь копирования. Содержит папки для копирования.
class FoldersForPath(Матрешка):

    def __init__(self, path: str):
        super().__init__()
        self.path = path

    def _how_much_done(done, not_done):
        if (done + not_done) <= 0:
            raise Exception("something went wrong")
        if done >= 0:
            return 1
        else:
            return 0


# Отдельная папка.
class Folder:

    def __init__(self, folder: str):
        self.status = "should be copied"
        self.folder = folder
