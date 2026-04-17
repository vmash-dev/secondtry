from homework import messages

input_name = input(messages.MSG_INPUT_NAME).strip().title()

if input_name.isalpha():
    print(messages.MSG_NAME_OK.format(name=input_name))
else:
    print(messages.MSG_NAME_ERROR)

input_age =input(messages.MSG_INPUT_AGE).strip().lstrip("0")

if input_age.isdigit():
    print(messages.MSG_AGE_OK.format(age=input_age))
else:
    print(messages.MSG_AGE_ERROR)

input_phone = input(messages.MSG_INPUT_PHONE).strip()

if input_phone.isdigit():
    print(messages.MSG_PHONE_OK.format(phone=input_phone))
else:
    print(messages.MSG_PHONE_ERROR)
print(messages.MSG_FINISH)