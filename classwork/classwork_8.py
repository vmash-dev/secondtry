apples = "3"
pears = "2"
print(type(apples))

apples = int(apples)
print(type(apples))

integer_number = 1000
integer_number2 = 10_001
summa = integer_number + integer_number2
print(summa)
print("Сума:", summa, 'in total')
print(f"{summa=}")
print(f"{2+2=}")
pears = int(pears)

total_fruits = apples + pears
# total_fruits_cost = total_fruits * "156"

print(total_fruits)

n5 = 20
n6 = 5
fraction = n5 / n6
print(f"{fraction=}")

not_integer = 5.0
not_integer2 = 5.0
not_integer_summa = not_integer + not_integer2 + integer_number2
print(f"{not_integer_summa=}")

# bananas_quantity = input('Enter the number of bananas: ')
# bananas_quantity = float(bananas_quantity)
# banana_cost_per_unit = 100
# total_bananas_cost = bananas_quantity * banana_cost_per_unit
# print(f"{total_bananas_cost=}")
bananas_quantity = round(126.65, -1)
print(bananas_quantity)