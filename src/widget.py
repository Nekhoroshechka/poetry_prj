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


def get_data(enter_data: str) -> str:
    """Функция форматирует дату"""
    slise_of_enter_data = enter_data[:10]
    list_data = slise_of_enter_data.split("-")
    list_data_reverse = list_data[::-1]
    correct_data = ".".join(list_data_reverse)
    return correct_data
