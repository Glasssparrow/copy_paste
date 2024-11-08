

# Создать класс команды на копирование.
# Order переименовать в Rule во избежание путаницы.

# Класс должен содержать всю необходимую информацию для копирования.
# Класс должен содержать всю необходимую информацию о результатах копирования.

# Учесть что класс должен содержать информацию о том на какие папки
# поступал приказ копировать (они были выделены), а на какие - нет.


class Common:

    def __init__(self):
        self.data = []
        self.status = "should be copied"


class Order111:

    def __init__(self):
        pass


class RulesForName:

    def __init__(self):
        pass


class PathsForRule:

    def __init__(self):
        pass


class FolderForPaths:

    def __init__(self):
        pass


class Folder:

    def __init__(self):
        pass


