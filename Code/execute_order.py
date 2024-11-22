

def copy_files(order):
    for rules_for_file in order.data:
        for paths_for_rule in rules_for_file.data:
            for folders_for_path in paths_for_rule.data:
                for folder in folders_for_path.data:
                    pass
