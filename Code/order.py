from Code.CONSTANTS import (
    SHOULD_BE_COPIED,
    SHOULD_BE_COPIED_PARTIALLY,
    SHOULD_NOT_BE_COPIED,
    SUCCESSFUL,
    PARTIALLY_SUCCESSFUL,
    NOT_SUCCESSFUL,
    WASNT_COPIED,
    WAS_COPIED,
    YES,
)


class Матрешка:

    def __init__(self):
        self.data = []
        self.status = SHOULD_BE_COPIED

    def ask_status(self):
        successful = 0
        not_successful = 0
        first_iteration = True
        was_copied = None
        for element in self.data:
            if first_iteration:
                if element.status in WAS_COPIED:
                    was_copied = True
                else:
                    was_copied = False
            if element.status in YES:
                successful += 1
            else:
                not_successful += 1
            # Если статус (задание/результат) элемента не
            # совпадает со статусом первого элемента, значит
            # случилась какая-то путаница.
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
        done = self._how_much_done(successful, not_successful)
        if was_copied:
            if done == 0:
                self.status = NOT_SUCCESSFUL
            elif 0 < done < 1:
                self.status = PARTIALLY_SUCCESSFUL
            elif done == 1:
                self.status = SUCCESSFUL
        else:
            if done == 0:
                self.status = SHOULD_NOT_BE_COPIED
            elif 0 < done < 1:
                self.status = SHOULD_BE_COPIED_PARTIALLY
            elif done == 1:
                self.status = SHOULD_BE_COPIED

    def _how_much_done(self, done, not_done):
        self._validate_done_not_done(done, not_done)
        result = done/(done+not_done)
        return result

    @staticmethod
    def _validate_done_not_done(done, not_done):
        if (done + not_done) <= 0:
            raise Exception("something went wrong")

    def _validate_key(self, key):
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


# Отдельный путь копирования. Содержит папки для копирования.
class FoldersForPath(Матрешка):

    def __init__(self, path: str):
        super().__init__()
        self.path = path

    def _how_much_done(self, done, not_done):
        self._validate_done_not_done(done, not_done)
        result = done / (done + not_done)
        if result > 0:
            return 1
        return result


# Отдельная папка.
class Folder:

    def __init__(self, folder: str):
        self.status = SHOULD_BE_COPIED
        self.folder = folder

    def set_status(self, result):
        if result:
            self.status = SUCCESSFUL
        else:
            self.status = NOT_SUCCESSFUL


def spread_order_status(order):
    for rules_for_file in order.data:
        for paths_for_rule in rules_for_file.data:
            for folders_for_path in paths_for_rule.data:
                folders_for_path.ask_status()
            paths_for_rule.ask_status()
        rules_for_file.ask_status()
