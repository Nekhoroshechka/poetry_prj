# Проект "Серверная часть виджета банковских операций клиента"

## Описание:

Виджет имеет возможность отображать операции клиента.

## Установка:

1. Клонируйте репозиторий:
```commandline
git clone https://github.com/Nekhoroshechka/poetry_prj.git
```
2. Установите зависимости:
```commandline
poetry install
```

## Пример использования:
Для того, чтобы запустить проект, необходимо сначала установить зависимости.
Затем запустите файл main.py, к примеру через командную строку:
```commandline
python main.py
```
В файле main.py уже подготовлены примеры для демонстрации работы функций.

## Тестирование
Все функции протестированы через pytest, для запуска выполните команду:
```commandline
pytest
```
Чтобы посмотреть на сколько процентов функциональный код  покрыт тестами, 
наберите команду:
```commandline
poetry run pytest --cov
```
## Новый модуль generators.py содержит три функции:

1. filter_by_currency - Функция возвращает итератор, где валюта соответствует заданной в параметре.

# Пример использования:
```commandline
usd_transactions = filter_by_currency(transactions, "USD")
for i in range(2):
    print(next(usd_transactions))

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
```

2. transaction_descriptions - Функция возвращает описания для транзакций.

# Пример использования:
```commandline
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```

3. card_number_generator - Генератор номеров карт формата 'ХХХХ ХХХХ ХХХХ ХХХХ' в заданном числовом диапозоне
 
# Пример использования:
```commandline
for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```

## Новый модуль decorators.py содержит декоратор @log, который регистрирует детали выполнения функций.

# Пример использования:
```commandline
@log(None)
def my_function(x, y):
    return x + y


my_function(1, 2)
>>> my_function ok
```
Так как у данного декоратора параметр не является именем текстового файла, результат выдается в консоль.