from os import path
from Code.copy_folder_or_file import (
    copy_folder,
    copy_file,
)


def copy_files(order, project_folder, source_folder):
    for rules_for_file in order.data:
        for paths_for_rule in rules_for_file.data:
            for folders_for_path in paths_for_rule.data:
                for folder in folders_for_path.data:
                    target = path.join(
                        folders_for_path.path,
                        project_folder,
                        folder.folder,
                        rules_for_file.name,
                    )
                    source = path.join(
                        source_folder,
                        rules_for_file.name,
                    )
                    if rules_for_file.is_folder:
                        copy_folder(source, target)
                    else:
                        copy_file(source, target)
