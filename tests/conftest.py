import pytest

@pytest.fixture
def card_numbers():
    return ['1596837868705199', '7158300734726758', '6831982476737658']


@pytest.fixture
def account_numbers():
    return ['64686473678894779589', '35383033474447895560', '73654108430135874305']


@pytest.fixture
def customer_details():
    return [
        'Maestro 1596837868705199',
        'Счет 64686473678894779589',
        'MasterCard 7158300734726758',
        'Счет 35383033474447895560',
        'Visa Classic 6831982476737658',
        'Visa Platinum 8990922113665229',
        'Visa Gold 5999414228426353',
        'Счет 73654108430135874305']

@pytest.fixture
def enter_data():
    return [
        '2024-03-11T02:26:18.671407',
        '2018-06-30T02:08:58.425572',
        '2018-09-12T21:27:25.241689']
