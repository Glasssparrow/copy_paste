from Code.order import *


def add_element_to_order(order, element, is_folder: bool):
    pass


def get_order(rules, folders, files):
    order = Order()
    for folder in folders:
        add_element_to_order(order, folder, True)
    for file in files:
        add_element_to_order(order, file, False)
