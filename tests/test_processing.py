import pytest
from src.processing import filter_by_state, sort_by_date


# Тестирование функции фильтрации списка словарей
def test_filter_by_state(list_of_dicts):
    assert filter_by_state(list_of_dicts) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]


def test_filter_by_state_without_state(list_of_dicts):
    assert filter_by_state([
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}], 'CANCEL') == []


@pytest.mark.parametrize('state, expected', [
    ('CANCELED', [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]),
    ('EXECUTED', [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}])
])
def test_filter_by_state_other(list_of_dicts,state, expected):
    assert filter_by_state(list_of_dicts, state=state) == expected


def test_filter_by_state_empty():
    assert filter_by_state([]) == 'Введено некорректное значение'


# Тестирование функции сортировки списка словарей по датам
@pytest.mark.parametrize('sorting_direction, expected', [
    (True, [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    (False, [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])
])
def test_sort_by_data(list_of_dicts, sorting_direction, expected):
    assert sort_by_date(list_of_dicts, sorting_direction=sorting_direction) == expected


def test_sort_by_data_same_data(list_of_dicts):
    assert sort_by_date([
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-06-30T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2018-06-30T18:35:29.512364'}]
    ) == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-06-30T21:27:25.241689'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2018-06-30T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T08:21:33.419441'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.mark.parametrize('list_of_dicts, expected', [
    ([
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019.07.03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018.10.14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018.09.12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018.06.30T02:08:58.425572'}],
[
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019.07.03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018.10.14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018.09.12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018.06.30T02:08:58.425572'}
    ]),
    ([
        {'id': 939719570, 'state': 'EXECUTED', 'date': '20180630T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '20180912T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '20181014T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '20190703T18:35:29.512364'}],
    [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '20190703T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '20181014T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '20180912T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '20180630T02:08:58.425572'}])
])
def test_sort_by_data_non_standard(list_of_dicts, expected):
    assert sort_by_date(list_of_dicts) == expected


def test_sort_by_data_empty(list_of_dicts):
    assert sort_by_date([
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': ''},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2018-06-30T18:35:29.512364'}]
    ) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2018-06-30T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T08:21:33.419441'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': ''}]
