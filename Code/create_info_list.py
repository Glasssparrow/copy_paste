from Code.CONSTANTS import (
    FULL_INFO,
    TARGET_FOLDERS,
    MASKS,
    NAMES_AND_RULES,
)


def get_info_list(mode, order, after_copying: bool):
    info_list = []
    for rules_for_file in order.data:
        if rules_for_file.is_folder:
            info_list.append(f"(папка){rules_for_file.name}")
        else:
            info_list.append(rules_for_file.name)
        for paths_for_rule in rules_for_file.data:
            if mode in [
                FULL_INFO,
                NAMES_AND_RULES,
            ]:
                info_list.append(paths_for_rule.rule.name)
            for folders_for_path in paths_for_rule.data:
                if mode in [
                    FULL_INFO,
                    TARGET_FOLDERS,
                    MASKS,
                ]:
                    info_list.append(folders_for_path.path)
                for folder in folders_for_path.data:
                    if mode in [
                        FULL_INFO,
                    ]:
                        info_list.append(folder.folder)
    info_list.reverse()  # Разворачиваем т.к. элементы добавлялись в конец
    return info_list
