from pywebio.input import input
from pywebio.output import put_markdown
while True:
    number_1 = input("Введи первое число:").strip()
    number_2 = input("Введи второе число:").strip()
    if number_1.isdigit():
        number_1 = int(number_1)
        if number_2.isdigit():
            number_2 = int(number_2)
            suma = number_1 + number_2
            minus = number_1 - number_2
            multiply = number_1 * number_2
            podelit = number_1 / number_2
            put_markdown("## Ответ:")
            put_markdown("---")
            put_markdown(f"# Сума: {suma}")
            put_markdown(f"# Вычитание: {minus}")
            put_markdown(f"# Умножение: {multiply}")
            put_markdown(f"# Деление: {podelit}")
            put_markdown("---")
        else:
            put_markdown("## Нормально напиши")
            put_markdown("---")
    else:
        put_markdown("## Нормально напиши")
        put_markdown("---")
