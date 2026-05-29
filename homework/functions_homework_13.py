def get_two_numbers(number_1: int | float, number_2: int | float, operation: str = "sum") -> int | float:
    if operation == "sum":
        sum_result = number_1 + number_2
        return sum_result
    else:
        difference = number_1 - number_2
        return difference

def get_string(string_1: str, upper: bool = True) -> str:
    if upper:
        return string_1.upper()
    else:
        return string_1.lower()

def get_sum_of_numbers(text: str, separator: str = ",") -> int:
    parts = text.split(separator)

    total = 0
    for i in parts:
        total += int(i)

    return total
