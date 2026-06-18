from typing import Callable
from functools import wraps


def decorator_check_int_number(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == int:
            result += 10
        return result

    return wrapper


@decorator_check_int_number
def add_numbers(number_1: int | float, number_2: int | float) -> int | float:
    result = number_1 + number_2
    return result


result_1 = add_numbers(67, 1488)
print(result_1)

result_2 = add_numbers(52.6767, 67.5252)
print(result_2)
