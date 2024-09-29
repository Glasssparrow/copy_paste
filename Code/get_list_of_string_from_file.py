

def get_list_of_strings_from_file(path):
    result = []
    # Читаем файл
    file = open(path, "r", encoding="utf-8")
    try:
        text = file.read()
    except Exception:
        raise Exception(
            f"Не найден/не удалось прочитать файл {path}"
        )
    finally:
        file.close()
    # Делим текст на строки
    text_list = text.split("\n")
    for line in text_list:
        # Пропускаем строку если она пуста, иначе удаляем пустоты
        if not line.strip():
            continue
        else:
            value = line.strip()
        # Если текст начинается с # - это комментарий, пропускаем.
        if value[0] == "#":
            continue
        result.append(value)
    return result
