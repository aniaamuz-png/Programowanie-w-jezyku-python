def is_palindrome(text: str) -> bool:
    new_text = text.lower()
    return new_text == new_text[::-1]


