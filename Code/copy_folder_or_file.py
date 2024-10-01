import shutil
import os


def copy_folder(source_path, target_path):
    if os.path.isdir(target_path):
        shutil.rmtree(target_path)
    shutil.copytree(source_path, target_path)


def copy_file(source_path, target_path):
    shutil.copy(source_path, target_path)
