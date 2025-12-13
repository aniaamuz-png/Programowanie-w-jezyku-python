from functions_for_testing import is_palindrome

def test_kajak():
    assert is_palindrome("kajak") is True


def test_sentence_palindrome():
    assert is_palindrome("Kobyła ma mały bok") is True


def test_not_palindrome():
    assert is_palindrome("python") is False


def test_empty_string():
    assert is_palindrome("") is True


def test_single_character():
    assert is_palindrome("A") is True