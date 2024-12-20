from Code.order import (
    RulesForName,
    PathsForRule,
    FoldersForPath,
    Folder,
)
from os.path import basename, dirname, join


def add_element_to_order(
            rules, order,
            element, is_folder,
            source_folder,
        ):
    folder_or_file = RulesForName(
        name=element, is_folder=is_folder, path=source_folder,
    )
    order.append(folder_or_file)
    for rule in rules:
        paths_for_rule = PathsForRule(rule=rule)
        folder_or_file.append(paths_for_rule)
        for path in rule.target:
            folders_for_path = FoldersForPath(path)
            paths_for_rule.append(folders_for_path)
            for folder in rule.folders_options:
                folder_option = Folder(folder)
                folders_for_path.append(folder_option)


def process_element(
        rules, source_folder,
        order, element, is_folder: bool
):
    element_name = basename(element)
    element_dir = dirname(element)
    path_to_element = join(source_folder, element_dir)
    rules_should_be_applied = []
    for rule in rules:
        if rule.should_be_copied(element_name, is_folder):
            rules_should_be_applied.append(rule)
    if rules_should_be_applied:
        add_element_to_order(
            rules=rules_should_be_applied, order=order,
            element=element_name, is_folder=is_folder,
            source_folder=path_to_element,
        )


def fill_order(order, rules, folders, files, source_folder):
    for folder in folders:
        process_element(
            rules=rules, order=order,
            element=folder, is_folder=True,
            source_folder=source_folder,
        )
    for file in files:
        process_element(
            rules=rules, order=order,
            element=file, is_folder=False,
            source_folder=source_folder,
        )
