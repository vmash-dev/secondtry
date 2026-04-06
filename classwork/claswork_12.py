numbers = [1, 3, 4]
names = ['Anna', "Ivan"]
mixed = [
    1,
    90.901,
    True,
    False,
    "some text",

    ['123', 1232],

]

first_element = mixed[0]
print(first_element)

third_element = mixed[2]
print(third_element)

last_element = mixed[-1]
print(last_element)

last_element_in_last_element = last_element[-1]
print(last_element_in_last_element)
# change lists
string = '123'
print(id(string))
string = string + '1'
print(id(string))

number = 123
print(id(number))
number = number + 1
print(id(number))
