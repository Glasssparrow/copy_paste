import os


def list_dir(relative_path):
    # Просто функция из os, но поднимающая ошибку с моим описанием.
    try:
        filenames = os.listdir(relative_path)
    except Exception:
        raise Exception(
                f"Не удается найти относительный путь {relative_path}"
            )
    return filenames


def get_list_of_folders_names(relative_path):
    # получаем лист файлов и папок из директории
    filenames = list_dir(relative_path)

    result = []
    for filename in filenames:
        # Получаем путь к файлу/папке
        path = os.path.join(
            os.path.abspath(relative_path), filename
        )
        # Проверяем ведет ли путь к папке, если да - добавляем.
        if os.path.isdir(os.path.join(
                relative_path, filename
        )):
            result.append(filename)
    result.sort()
    return result


def get_list_of_files_names(relative_path):
    # получаем лист файлов и папок из директории
    filenames = list_dir(relative_path)

    result = []
    for filename in filenames:
        # Получаем путь к файлу/папке
        path = os.path.join(
            os.path.abspath(relative_path), filename
        )
        # Проверяем ведет ли путь к папке, если нет - добавляем.
        if not os.path.isdir(os.path.join(
                relative_path, filename
        )):
            result.append(filename)
    result.sort()
    return result
