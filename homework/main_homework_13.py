from functions_homework_13 import get_two_numbers, get_string, get_sum_of_numbers

print(get_two_numbers(3, 2, "sub"))
print(get_two_numbers(number_1=6, number_2=7, operation="sum"))
data = {
    "number_1": 10,
    "number_2": 12,
    "operation": "sum"
}
print(get_two_numbers(**data))

print(get_string("kukuzyambra","True"))
print(get_string(string_1="kukuzyambra", upper=False))
data = {
    "string_1": "kukuzyambra",
    "upper": False,
}
print(get_string(**data))

print(get_sum_of_numbers("4,9,1"))
print(get_sum_of_numbers(text="5,8,3", separator=","))
data = {
    "text": "2,6,7",
    "separator": ","
}

print(get_sum_of_numbers(**data))
