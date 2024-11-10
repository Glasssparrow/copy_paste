from Code.order import *


def add_element_to_order(rules, order, element, is_folder: bool):
    for rule in rules:
        if rule.should_be_copied(element, is_folder):
            pass


def get_order(rules, folders, files):
    order = Order()
    for folder in folders:
        add_element_to_order(
            rules=rules, order=order,
            element=folder, is_folder=True,
        )
    for file in files:
        add_element_to_order(
            rules=rules, order=order,
            element=file, is_folder=False,
        )
