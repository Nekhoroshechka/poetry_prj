from typing import Any


# Создаем новый список отфильтрованных по аргументу 'value_of_state' словарей
# перебираем словари в списке - если ключу 'state' соответствует значение state из функции,
# то добавляем в список этот словарь
# по завершению перебора выводится список с отобранными по условию словарями
def filter_by_state(list_of_dicts: list[dict], state: str = "EXECUTED") -> Any:
    """Функция возвращает список словарей, у которых ключ state соответствует указанному значению"""
    if list_of_dicts == list():
        return "Введено некорректное значение"
    new_list = list()
    for item in list_of_dicts:
        if item.get("state") == state:
            new_list.append(item)
    return new_list


def sort_by_date(list_of_dicts: list[dict], sorting_direction: bool = True) -> list[dict]:
    """Функция сортирует по дате список словарей"""
    sorted_dicts = sorted(list_of_dicts, key=lambda dictionary: dictionary["date"], reverse=sorting_direction)
    return sorted_dicts
