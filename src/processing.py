def filter_by_state(list_of_dicts: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает список словарей, у которых ключ state соответствует указанному значению"""
    # новый список отфильтрованных по аргументу 'value_of_state' словарей
    new_list = list()
    # перебираем словари в списке - если ключу 'state' соответствует значение state из функции,
    # то добавляем в список этот словарь
    # по завершению перебора выводится список с отобранными по условию словарями
    for item in list_of_dicts:
        if item.get("state") == state:
            new_list.append(item)
    return new_list


def sort_by_date(list_of_dicts: list[dict], sorting_direction: bool = True) -> list[dict]:
    """Функция сортирует по дате список словарей"""
    sorted_dicts = sorted(list_of_dicts, key=lambda dictionary: dictionary["date"], reverse=sorting_direction)
    return sorted_dicts
