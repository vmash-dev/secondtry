numbers = [3, 7, 2, 9, 4, 6, 1, 8]

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

doubled_even = []
for number in even_numbers:
    doubled_even.append(number * 2)

if 8 in doubled_even:
    doubled_even.remove(8)

print(f"Парні числа: {even_numbers}")
print(f"Подвоєні парні (без 8): {doubled_even}")
