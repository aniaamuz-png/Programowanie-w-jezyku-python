import pytest

from functions_for_testing import calculate_discount


def test1():
    assert calculate_discount(100, 0.2) == 80.00


def test2():
    assert calculate_discount(50, 0) == 50.00


def test3():
    assert calculate_discount(200, 1) == 0.00


def test4():
    with pytest.raises(ValueError):
        calculate_discount(100, -0.1)


def test5():
    with pytest.raises(ValueError):
        calculate_discount(100, 1.5)
