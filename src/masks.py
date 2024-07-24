def get_mask_card_number(card_number: str) -> str:
    """Возвращает маску карты при получении номера карты"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Возвращает маску номера счета, полученного на входе функции"""
    return f"**{account_number[-4:]}"
