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

from src.masks import get_mask_account
from src.masks import get_mask_card_number

# user_card_number = input("Введите номер карты: ")
# user_account_number = input("Введите номер счета: ")

#Задание 2
# Проверка работы функции, которая умеет обрабатывать информацию о картах и счетах
# Пример для карты
# Visa Platinum 7000792289606361  # входной аргумент
# Visa Platinum 7000 79** **** 6361  # выход функции

# Пример для счета
# Счет 73654108430135874305   входной аргумент
# Счет **4305   выход функции

from src.widget import mask_account_card
from src.widget import get_data

if __name__ == "__main__":
    print(mask_account_card('Visa Platinum 7000792289606361'))
    print(mask_account_card('Maestro 1596837868705199'))
    print(mask_account_card('Счет 64686473678894779589'))
    print(mask_account_card('MasterCard 7158300734726758'))
    print(mask_account_card('Счет 35383033474447895560'))
    print(mask_account_card('Visa Classic 6831982476737658'))
    print(mask_account_card('Visa Platinum 8990922113665229'))
    print(mask_account_card('Visa Gold 5999414228426353'))
    print(mask_account_card('Счет 73654108430135874305'))
    print(get_data("2024-03-11T02:26:18.671407"))
