import os


def get_list_of_folders_names(directory_name):
    # get all files' and folders' names in the current directory
    filenames = os.listdir(directory_name)

    result = []
    for filename in filenames:  # loop through all the files and folders
        path = os.path.join(
            os.path.abspath(directory_name), filename
        )
        if os.path.isdir(os.path.join(
                directory_name, filename
        )):  # check whether the current object is a folder or not
            result.append(filename)

    result.sort()
    return result


def get_list_of_files_names(directory_name):
    # get all files' and folders' names in the current directory
    filenames = os.listdir(directory_name)

    result = []
    for filename in filenames:  # loop through all the files and folders
        path = os.path.join(
            os.path.abspath(directory_name), filename
        )
        if not os.path.isdir(os.path.join(
                directory_name, filename
        )):  # check whether the current object is a folder or not
            result.append(filename)

    result.sort()
    return result
