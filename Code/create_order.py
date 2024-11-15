from Code.order import *


def add_element_to_order(
            rules=rules, order=order,
            element=folder, is_folder=True,
            source_folder=source_folder,
        ):
    pass


def process_element(
        rules, source_folder,
        order, element, is_folder: bool
):
    rules_should_be_applyed = []
    for rule in rules:
        if rule.should_be_copied(element, is_folder):
            rules_should_be_applyed.append(rule)
    if rules_should_be_applyed:
        add_element_to_order(
            rules=rules_should_be_applyed, order=order,
            element=folder, is_folder=True,
            source_folder=source_folder,
        )


def get_order(rules, folders, files, source_folder):
    order = Order()
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
