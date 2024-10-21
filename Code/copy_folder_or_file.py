import shutil
import os


def copy_folder(source_path, target_path):
    # TODO
    # Добавить проверку существования директории перед копирование.
    # Чтобы программа не создавала несуществующей папки.
    
    # Проверяем что такой папки еще нет, если есть - удаляем.
    # Это нужно чтобы избежать исключения при копировании.
    if os.path.isdir(target_path):
        shutil.rmtree(target_path)
    shutil.copytree(source_path, target_path)


def copy_file(source_path, target_path):
    shutil.copy(source_path, target_path)
