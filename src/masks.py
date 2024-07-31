def get_mask_card_number(card_number: str) -> str:
    """Возвращает маску карты при получении номера карты"""
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return "Введено некорректное значение номера карты"


def get_mask_account(account_number: str) -> str:
    """Возвращает маску номера счета, полученного на входе функции"""
    if len(account_number) == 20 and account_number.isdigit():
        return f"**{account_number[-4:]}"
    else:
        return "Введено некорректное значение номера счета"
