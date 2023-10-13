import pytest
from Factory import Factory
from RectangleCollision import RectangleCollision
from Storage import Storage


@pytest.fixture(scope="module")
def app():
    app = Factory.create(RectangleCollision)
    yield app


@pytest.fixture(scope="module")
def storage():
    storage = Storage()
    yield storage


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


def test_storage_get_about(storage):
    result = storage.get_about()
    type(result) == str


def test_storage_get_version(storage):
    result = storage.get_version()
    type(result) == str


def test_storage_get_help(storage):
    result = storage.get_help()
    type(result) == str
