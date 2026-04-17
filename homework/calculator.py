from pywebio.input import input, select
from pywebio.output import put_markdown
while True:
    number_1 = input("Введи первое число:").strip()
    count = select("Введи действие:", ['+', '-', '*', '/'])
    number_2 = input("Введи второе число:").strip()
    if number_1.isdigit():
        number_1 = int(number_1)
        if number_2.isdigit():
            number_2 = int(number_2)
            if count == "+":
                suma = number_1 + number_2
                put_markdown(f"## {number_1} + {number_2} = {suma}")
            if count == "-":
                minus = number_1 - number_2
                put_markdown(f"## {number_1} - {number_2} = {minus}")
            if count == "*":
                multiply = number_1 * number_2
                put_markdown(f"## {number_1} * {number_2} = {multiply}")
            if count == "/":
                podelit = number_1 / number_2
                put_markdown(f"## {number_1} / {number_2} = {podelit}")
        else:
            put_markdown("## Нормально напиши")
            put_markdown("---")
    else:
        put_markdown("## Нормально напиши")
        put_markdown("---")
