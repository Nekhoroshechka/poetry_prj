import pytest
from src.masks import get_mask_card_number, get_mask_account


# Тестируем функцию маски карты
def test_get_mask_card_number(card_numbers):
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'


@pytest.mark.parametrize('card_numbers, expected', [
    ('1596837868705199', '1596 83** **** 5199'),
    ('715830073472675', 'Введено некорректное значение номера карты'),
    ('68319824767376588', 'Введено некорректное значение номера карты')
])
def test_get_mask_card_numbers(card_numbers, expected):
    assert get_mask_card_number(card_numbers) == expected


def test_get_mask_card_number_empty():
    assert get_mask_card_number('') == 'Введено некорректное значение номера карты'


def test_get_mask_card_number_invalid_card_number():
    assert get_mask_card_number('XTA6837868705199') == 'Введено некорректное значение номера карты'


# Тестируем функцию маски счета
def test_get_mask_account(account_numbers):
    assert get_mask_account('73654108430135874305') == '**4305'


@pytest.mark.parametrize('account_numbers, expected', [
    ('64686473678894779589', '**9589'),
    ('3538303347444789556', 'Введено некорректное значение номера счета'),
    ('736541084301358743055', 'Введено некорректное значение номера счета')
])
def test_get_mask_accounts(account_numbers, expected):
    assert get_mask_account(account_numbers) == expected


def test_get_mask_accounts_invalid_account_number():
    assert get_mask_account('6468XXXX678894779589') == 'Введено некорректное значение номера счета'
