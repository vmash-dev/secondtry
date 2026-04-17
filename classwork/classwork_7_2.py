from homework import messages

# from messages import MSG_INPUT_BREAD_QUANTITY


bread_quantity = input(messages.MSG_INPUT_BREAD_QUANTITY).strip().lstrip("0")
print(bread_quantity)
#
is_correct_bread_quantity = bread_quantity.isdigit()
# print(is_correct_bread_quantity)
is_space_big = True
false = False

if is_space_big:
    print("la-la")

if is_correct_bread_quantity:
    print(messages.MSG_CORRECT_INPUT)
else:
    print(messages.MSG_INCORRECT_INPUT)

# is_only_letters = bread_quantity.isalpha()
# print(is_only_letters)

# is_only_ascii= bread_quantity.isascii()
# print(is_only_ascii)

is_lower = bread_quantity.islower()
print(is_lower)

is_start_with = bread_quantity.startswith("123")
print(is_start_with)

print(messages.MSG_FINISH)