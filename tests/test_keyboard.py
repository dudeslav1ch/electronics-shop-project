from src.keyboard import Keyboard
import pytest


@pytest.fixture
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(kb):
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang()
    assert str(kb.language) == "EN"


def test_name(kb):
    kb.name = 'Dark Project KD87A'

    assert kb.name == 'Dark Project KD87A'
