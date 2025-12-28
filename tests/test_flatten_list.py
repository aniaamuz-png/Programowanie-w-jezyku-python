import pytest

from functions_for_testing import flatten_list


def test_1():
    assert flatten_list([1, 2, 3]) == [1, 2, 3]


def test_2():
    assert flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]


def test_3():
    assert flatten_list([]) == []


def test_4():
    assert flatten_list([[[1]]]) == [1]


def test_5():
    assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]
