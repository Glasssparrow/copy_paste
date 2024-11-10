from Code.order import *


def add_element_to_order(
        rules, source_folder,
        order, element, is_folder: bool
):
    for rule in rules:
        if rule.should_be_copied(element, is_folder):
            paths = order.get_paths(
                directory=source_folder,
                is_folder_and_not_a_file=is_folder,
                name_of_file_or_folder=element,
            )


def get_order(rules, folders, files, source_folder):
    order = Order()
    for folder in folders:
        add_element_to_order(
            rules=rules, order=order,
            element=folder, is_folder=True,
            source_folder=source_folder,
        )
    for file in files:
        add_element_to_order(
            rules=rules, order=order,
            element=file, is_folder=False,
            source_folder=source_folder,
        )
