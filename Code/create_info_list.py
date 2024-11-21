from Code.CONSTANTS import (
    FULL_INFO,
    TARGET_FOLDERS,
    MASKS,
    NAMES_AND_RULES,
    ONLY_NAMES,
)


def get_info_list(mode, order):
    info_list = []
    for rules_for_file in order.data:
        for paths_for_rule in rules_for_file.data:
            for folders_for_path in paths_for_rule.data:
                for folder in folders_for_path.data:
                    pass
    return info_list
