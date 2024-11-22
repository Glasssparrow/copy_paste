import shutil
from os import path


def copy_folder(
        source_path, source_name,
        target_path, target_name,
):
    # Проверяем что такой папки еще нет, если есть - удаляем.
    # Это нужно, чтобы избежать исключения при копировании.
    target = path.join(
        target_path,
        target_name,
    )
    source = path.join(
        source_path,
        source_name,
    )
    if path.isdir(target_path):
        if path.isdir(target):
            shutil.rmtree(target)
        shutil.copytree(str(source), str(target))
        return True
    else:
        return False


def copy_file(
        source_path, source_name,
        target_path, target_name,
):
    target = path.join(
        target_path,
        target_name,
    )
    source = path.join(
        source_path,
        source_name,
    )
    if path.isdir(target_path):
        shutil.copy(str(source), str(target))
        return True
    else:
        return False
