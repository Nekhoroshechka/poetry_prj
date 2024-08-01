import pytest

from src.widget import get_data
from src.widget import mask_account_card


# Тестируем функцию обработки информации о картах и счетах
def test_mask_account_card(customer_details: str) -> None:
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Счет 35383033474447895560") == "Счет **5560"


@pytest.mark.parametrize(
    "customer_details, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_cards(customer_details: str, expected: str) -> None:
    assert mask_account_card(customer_details) == expected


def test_mask_account_card_invalid_card_or_account() -> None:
    with pytest.raises(ValueError):
        mask_account_card("Visa Classic 683198247673XXXX")
        mask_account_card("Счет 353830YYYY4447895560")
        mask_account_card("Metro 1596837868705199")


def test_mask_account_card_empty() -> None:
    assert mask_account_card("") == "Введено некорректное значение"


# Тестируем правильность преобразования даты
def test_get_data(enter_data: str) -> None:
    assert get_data("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize(
    "enter_data, expected",
    [
        ("20240311T02:26:18.671407", "Введен некорректный формат даты"),
        ("2024.03.11T02:26:18.671407", "Введен некорректный формат даты"),
        ("2024-03-1T02:26:18.671407", "Введен некорректный формат даты"),
    ],
)
def test_get_data_(enter_data: str, expected: str) -> None:
    assert get_data(enter_data) == expected


def test_get_data_empty() -> None:
    assert get_data("") == "Введено некорректное значение"
