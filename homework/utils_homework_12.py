def average(a: int | float, b: int | float, c: int | float) -> float:
    result = (a + b + c) / 3
    return round(result, 2)


def foo_check(something: int) -> bool:
    if something % 2 == 0 and something > 10:
        return True
    else:
        return False


def foo_vowels(text: str) -> int:
    vowels = "aeiouy"
    text_lower = text.lower()

    count = 0
    for char in text_lower:
        if char in vowels:
            count += 1

    return count