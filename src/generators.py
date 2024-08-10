import pytest
import sys


from typing import Iterator

# from typing import Generator, Any


def filter_by_currency(transaction_list: list[dict], code_of_currency: str) -> Iterator:
    """Функция возвращает итератор, где валюта соответствует заданной в параметре"""
    if not transaction_list:
        raise TypeError("Список транзакций пустой!")

    filtred_transactions = filter(
        lambda transaction: transaction.get("operationAmount").get("currency").get("code")
        == code_of_currency,
        transaction_list,
    )
    return filtred_transactions


    # if transaction_list != list():
    #     for transaction in transaction_list:
    #         if transaction["operationAmount"]["currency"]["code"] == code_of_currency:
    #             yield transaction
    # elif transaction_list["operationAmount"]["currency"]["code"] != code_of_currency:
    #     sys.exit("В транзакциях нет такого кода")
    # elif transaction_list == list():
    #     sys.exit("Нет транзакций")
    # raise AssertionError("Ввели пустой список!")


# if transactions == []:
#         sys.exit("Нет транзакций")
# for i in transactions:
#     if i.get("operationAmount").get("currency").get("code") != currency_code:
#         sys.exit("В транзакциях нет такого кода")
#     elif i.get("operationAmount").get("currency").get("code") == currency_code:
#         yield i
