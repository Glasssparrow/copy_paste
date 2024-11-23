from Code.CONSTANTS import (
    FULL_INFO,
    TARGET_FOLDERS,
    MASKS,
    NAMES_AND_RULES,
    ONLY_NAMES,
)


def _add_filename(
    info_list, rules_for_file,
    after_copying, mode,
):
    if rules_for_file.is_folder:
        info_list.append(f"(папка){rules_for_file.name}")
    else:
        info_list.append(rules_for_file.name)


def _add_rulename(
    info_list, paths_for_rule,
    after_copying, mode,
):
    if mode in [
        FULL_INFO,
        NAMES_AND_RULES,
    ]:
        info_list.append(paths_for_rule.rule.name)


def _add_path(
    info_list, folders_for_path,
    after_copying, mode,
):
    if mode in [
        FULL_INFO,
        TARGET_FOLDERS,
        MASKS,
    ]:
        info_list.append(folders_for_path.path)


def _add_folder(
    info_list, folder,
    after_copying, mode,
):
    if mode in [
        FULL_INFO,
    ]:
        info_list.append(folder.folder)


def get_info_list(mode, order, after_copying: bool):
    info_list = []
    for rules_for_file in order.data:
        _add_filename(
            info_list=info_list, rules_for_file=rules_for_file,
            after_copying=after_copying, mode=mode,
        )
        for paths_for_rule in rules_for_file.data:
            _add_rulename(
                info_list=info_list, paths_for_rule=paths_for_rule,
                after_copying=after_copying, mode=mode,
            )
            for folders_for_path in paths_for_rule.data:
                _add_path(
                    info_list=info_list,
                    folders_for_path=folders_for_path,
                    after_copying=after_copying, mode=mode,
                )
                for folder in folders_for_path.data:
                    _add_folder(
                        info_list=info_list, folder=folder,
                        after_copying=after_copying, mode=mode,
                    )
    info_list.reverse()  # Разворачиваем т.к. элементы добавлялись в конец
    return info_list
