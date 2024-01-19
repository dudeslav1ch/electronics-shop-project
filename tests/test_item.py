from src.item import Item
import pytest


@pytest.fixture
def fixture_item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def fixture_item_2():
    return Item("Ноутбук", 20000, 5)


def test_calculate_total_price(fixture_item, fixture_item_2):
    assert fixture_item.calculate_total_price() == 200000
    assert fixture_item_2.calculate_total_price() == 100000


def test_apply_discount(fixture_item, fixture_item_2):
    fixture_item.pay_rate = 0.8
    fixture_item.apply_discount()

    assert fixture_item.price == 8000.0
    assert fixture_item_2.price == 20000


def test_name(fixture_item):
    assert fixture_item.name == 'Смартфон'


def test_name_setter(fixture_item):
    fixture_item.name = 'СуперСмартфон'

    assert fixture_item.name == fixture_item.name[0:10]


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
