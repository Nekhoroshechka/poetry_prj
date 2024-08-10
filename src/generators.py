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


def transaction_descriptions(transaction_list: list[dict]) -> Iterator:
    for transaction in transaction_list:
        yield transaction["description"]
