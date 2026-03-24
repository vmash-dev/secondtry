import letter

client_name = input("Введіть ваше ім'я та прізвище: ").title().strip()
travel_date = input("Введіть дату поїздки: ").strip()
people = int(input("Введіть кількість осіб: "))

price = 15000
total = people * price

if people > 5:
    discount_amount = total * 0.05
else:
    discount_amount = 0

final_to_pay = total - discount_amount

final_message = letter.LETTER_TEMPLATE.format(
    name=client_name,
    date=travel_date,
    persons=people,
    price_per_person=price,
    total_price=total,
    discount=discount_amount,
    final_price=final_to_pay
)

print(final_message)
