import pytest

from functions_for_testing import fibonacci


def test_0():
    assert fibonacci(0) == 0


def test_1():
    assert fibonacci(1) == 1


def test_5():
    assert fibonacci(5) == 5


def test_10():
    assert fibonacci(10) == 55


def test_minus_1():
    with pytest.raises(ValueError):
        fibonacci(-1)
