from os import path
from Code.copy_folder_or_file import (
    copy_folder,
    copy_file,
)


def copy_files(order, project_folder):
    for rules_for_file in order.data:
        for paths_for_rule in rules_for_file.data:
            for folders_for_path in paths_for_rule.data:
                for folder in folders_for_path.data:
                    target_path = path.join(
                        folders_for_path.path,
                        project_folder,
                        folder.folder,
                    )
                    if rules_for_file.is_folder:
                        is_successful = copy_folder(
                            source_path=rules_for_file.path,
                            source_name=rules_for_file.name,
                            target_path=target_path,
                            target_name=rules_for_file.name,
                        )
                    else:
                        is_successful = copy_file(
                            source_path=rules_for_file.path,
                            source_name=rules_for_file.name,
                            target_path=target_path,
                            target_name=rules_for_file.name,
                        )
                    folder.set_status(is_successful)
