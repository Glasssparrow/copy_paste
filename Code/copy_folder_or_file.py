import shutil


def copy_folder(source_path, target_path):
    shutil.copytree(source_path, target_path)


def copy_file(source_path, target_path):
    shutil.copy(source_path, target_path)
