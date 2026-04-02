# №1
numbers = [1, 5, 2, 8, 3, 7]

max_num = numbers[0]
min_num = numbers[0]
total_sum = 0

for number in numbers:
    if number > max_num:
        max_num = number

    if number < min_num:
        min_num = number

    total_sum = total_sum + number

print(f"Найбільше: {max_num}, Найменше: {min_num}, Сума: {total_sum}")

print("-----------------------")

# №2
grades = [10, 8, 12, 7, 9]

total_sum = 0
for grade in grades:
    total_sum += grade

average = total_sum / len(grades)

above_average = []
for grade in grades:
    if grade > average:
        above_average.append(grade)

print(f"Список оцінок: {grades}")
print(f"Середній бал: {average}")
print(f"Оцінки вище середнього: {above_average}")