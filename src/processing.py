def filter_by_state(list_of_dicts: list[dict], state: str ='EXECUTED') -> list[dict]:
    """Функция возвращает список словарей, у которых ключ state соответствует указанному значению"""
    # новый список отфильтрованных по аргументу 'value_of_state' словарей
    new_list = list()
    # перебираем словари в списке - если ключу 'state' соответствует значение state из функции,
    # то добавляем в список этот словарь
    # по завершению перебора выводится список с отобранными по условию словарями
    for item in list_of_dicts:
        if item.get('state') == state:
            new_list.append(item)
    return new_list


print(filter_by_state(
[
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
], 'CANCELED')
)
