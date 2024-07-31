# В данной функции, в зависимости от входных данных, маскируется карта или счет.
# Чтобы "достать" из строки каждое слово по отдельности, применяю метод split.
# Затем запускаю перебор для определения какая функция будет применена исходя из условия: карта или счет.
# Чтобы на выходе вернулись все данные, полученные на входе, но с замаскированным счетом или картой,
# внутри цикла в каждом условии значение с номером счета(карты) заменяется внутри списка на замаскированное.
# На выходе получаем данные карты или счета замаскированные внутри функции.
def mask_account_card(customer_details: str) -> str:
    """Функция умеет обрабатывать информацию о картах и счетах"""
    from src.masks import get_mask_account
    from src.masks import get_mask_card_number

    if customer_details == "":
        return "Введено некорректное значение"
    else:
        words_list = customer_details.split()
        for word in words_list:
            if word in ["Maestro", "Visa", "MasterCard"]:
                if words_list[-1].isdigit() is False:
                    raise ValueError("Неверный номер карты")
                else:
                    user_card_number = words_list[-1]
                    masked_card = get_mask_card_number(user_card_number)
                    words_list[-1] = masked_card
                    result_mask_card = " ".join(words_list)
                return result_mask_card
            if word == "Счет" or word == "Счёт":
                if words_list[-1].isdigit() is False:
                    raise ValueError("Неверный номер счета")
                else:
                    user_account_number = words_list[-1]
                    masked_account = get_mask_account(user_account_number)
                    words_list[-1] = masked_account
                    result_mask_account = " ".join(words_list)
                return result_mask_account


# С помощью срезов выделяю в новую строку только те символы, которые нужны для форматирования даты.
# Пользуясь методом split, создаю список с разделением по символу "-".
# Возвращаясь к срезам, но уже внутри списка выстраиваю значения по формату даты шагом -1.
# Методом join склеиваю значения из списка обратно в строку, но в нужном порядке и с разделением ".".
def get_data(enter_data: str) -> str:
    """Функция форматирует дату"""
    if enter_data == "":
        return "Введено некорректное значение"
    else:
        slise_of_enter_data = enter_data[:10]
        if "-" not in slise_of_enter_data:
            return "Введен некорректный формат даты"
        else:
            list_data = slise_of_enter_data.split("-")
            for data_ in list_data:
                if data_.isdigit() is False:
                    return "Введен некорректный формат даты"
            list_data_reverse = list_data[::-1]
            correct_data = ".".join(list_data_reverse)
        return correct_data
