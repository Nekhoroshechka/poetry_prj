def mask_account_card(customer_details: str) -> str:
    """Функция умеет обрабатывать информацию о картах и счетах"""
    from src.masks import get_mask_account
    from src.masks import get_mask_card_number

    words_list = customer_details.split()
    for word in words_list:
        if word in ["Maestro", "Visa", "MasterCard"]:
            user_card_number = words_list[-1]
            masked_card = get_mask_card_number(user_card_number)
            words_list[-1] = masked_card
            result_mask_card = " ".join(words_list)
            return result_mask_card
        if word == "Счет" or word == "Счёт":
            user_account_number = words_list[-1]
            masked_account = get_mask_account(user_account_number)
            words_list[-1] = masked_account
            result_mask_account = " ".join(words_list)
            return result_mask_account
