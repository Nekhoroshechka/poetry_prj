# Задание
# Контекст
# IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает несколько
# последних успешных банковских операций клиента. Вам доверили реализовать этот проект, который на бэкенде будет
# готовить данные для отображения в новом виджете.
# Вы будете работать над проектом на протяжении всех домашних заданий этого курса.
# входной аргумент 7000792289606361
# выход функции 7000 79** **** 6361
# входной аргумент 73654108430135874305
# выход функции **4305

# from src.masks import get_mask_account
# from src.masks import get_mask_card_number

# user_card_number = input("Введите номер карты: ")
# user_account_number = input("Введите номер счета: ")

# Задание 2
# Проверка работы функции, которая умеет обрабатывать информацию о картах и счетах
# Пример для карты
# Visa Platinum 7000792289606361  # входной аргумент
# Visa Platinum 7000 79** **** 6361  # выход функции

# Пример для счета
# Счет 73654108430135874305   входной аргумент
# Счет **4305   выход функции

# from src.widget import get_data
# from src.widget import mask_account_card
from src.processing import filter_by_state
from src.processing import sort_by_date

if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
        )
    )
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
