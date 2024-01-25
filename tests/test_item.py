from src.item import Item
import pytest

from tests.test_phone import phone_1


@pytest.fixture
def item_1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item_2():
    return Item("Ноутбук", 20000, 5)


def test_calculate_total_price(item_1, item_2):
    assert item_1.calculate_total_price() == 200000
    assert item_2.calculate_total_price() == 100000


def test_apply_discount(item_1, item_2):
    item_1.pay_rate = 0.8
    item_1.apply_discount()

    assert item_1.price == 8000.0
    assert item_2.price == 20000


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr(item_1):
    assert repr(item_1) == "Item('Смартфон', 10000, 20)"


def test_str(item_1):
    assert str(item_1) == 'Смартфон'


def test_add(item_1, phone_1):
    assert item_1 + phone_1 == 25
    assert phone_1 + phone_1 == 10
