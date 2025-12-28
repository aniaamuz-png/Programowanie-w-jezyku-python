def is_palindrome(text: str) -> bool:
    new_text = text.lower()
    return new_text == new_text[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("potrzebna liczba nieujemna")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def count_vowels(text: str) -> int:
    vowels = "aeiouyó"
    return sum(1 for ch in text.lower() if ch in vowels)


def calculate_discount(price: float, discount: float) -> float:
    if not 0 <= discount <= 1:
        raise ValueError("Zniżka pomiędzy 0 a 1")
    return price * (1 - discount)
