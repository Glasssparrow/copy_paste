import os


def list_dir(relative_path):
    try:
        filenames = os.listdir(relative_path)
    except Exception:
        raise Exception(
                f"Не удается найти относительный путь {relative_path}"
            )
    return filenames


def get_list_of_folders_names(relative_path):
    # get all files' and folders' names in the current directory
    filenames = list_dir(relative_path)

    result = []
    for filename in filenames:  # loop through all the files and folders
        path = os.path.join(
            os.path.abspath(relative_path), filename
        )
        if os.path.isdir(os.path.join(
                relative_path, filename
        )):  # check whether the current object is a folder or not
            result.append(filename)

    result.sort()
    return result


def get_list_of_files_names(relative_path):
    # get all files' and folders' names in the current directory
    filenames = list_dir(relative_path)

    result = []
    for filename in filenames:  # loop through all the files and folders
        path = os.path.join(
            os.path.abspath(relative_path), filename
        )
        if not os.path.isdir(os.path.join(
                relative_path, filename
        )):  # check whether the current object is a folder or not
            result.append(filename)

    result.sort()
    return result
