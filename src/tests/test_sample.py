import pytest
from RectangleCollision import RectangleCollision


@pytest.fixture(scope="module")
def app():
    app = RectangleCollision()
    yield app


def test_empty_entry_validation(app):
    result = app._entry_input_validate("")
    assert result == False


def test_symbol_entry_validation(app):
    result = app._entry_input_validate("asd")
    assert result == False


def test_negative_entry_validation(app):
    result = app._entry_input_validate("-1")
    assert result == False


def test_null_entry_validation(app):
    result = app._entry_input_validate("0")
    assert result == False


def test_positive_entry_validation(app):
    result = app._entry_input_validate("1")
    assert result == True


def test_overflow_entry_validation(app):
    result = app._entry_input_validate("10")
    assert result == False


def test_float_entry_validation(app):
    result = app._entry_input_validate("0.1")
    assert result == False
