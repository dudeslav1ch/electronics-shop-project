from src.phone import Phone
import pytest


@pytest.fixture
def phone_1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_repr(phone_1):
    assert repr(phone_1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(phone_1):
    phone_1.number_of_sim = 2
    assert phone_1.number_of_sim == 2

    phone_1.number_of_sim = 0
    assert phone_1.number_of_sim == 2
