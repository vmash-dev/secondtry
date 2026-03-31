from pywebio.input import input, slider, select
from pywebio.output import put_markdown, put_text, put_image, put_error
import pictures_2
import prices_2
from discount_2 import DISCOUNT_TRIGGER_PEOPLE, DISCOUNT_PERCENTAGE

put_markdown("# 🏔️ Організатор подорожі в Карпати")
put_image(pictures_2.PICTURE_CARPATHIANS)
put_markdown("---")

students = input("Скільки поїде учнів?", type="number", min=0, value=1)
teachers = input("Скільки поїде вчителів?", type="number", min=0, value=1)

if students == 0:
    put_error("Помилка! Поїздка неможлива без учнів.")
else:
    transport_type = select("Оберіть транспорт:", ['🚌 Автобус', '🚆 Поїзд'])
    days = slider("На скільки днів поїздка?", min_value=0, max_value=14, value=2)

    total_people = students + teachers

    cost_transport = 0
    buses_count = 0

    if transport_type == '🚌 Автобус':
        put_image(pictures_2.PICTURE_BUS, width="300")
        buses_count = total_people // prices_2.BUS_CAPACITY
        if total_people % prices_2.BUS_CAPACITY > 0:
            buses_count += 1
        cost_transport = buses_count * prices_2.PRICE_BUS
    else:
        put_image(pictures_2.PICTURE_TRAIN, width="300")
        cost_transport = total_people * prices_2.PRICE_TRAIN

    cost_hotel = 0
    if days > 0:
        cost_hotel = total_people * prices_2.PRICE_HOTEL_NIGHT * days

    total_cost = cost_transport + cost_hotel

    discount_summa = 0
    if total_people > DISCOUNT_TRIGGER_PEOPLE:
        discount_summa = round(total_cost * DISCOUNT_PERCENTAGE / 100, 0)

    final_cost = total_cost - discount_summa

    put_markdown("## 📋 РЕЗУЛЬТАТ РОЗРАХУНКУ:")

    put_text(f"👥 Загальна кількість людей: {total_people}")

    if buses_count:
        put_text(f"🚌 Кількість автобусів: {buses_count} шт.")

    put_text(f"🎫 Вартість транспорту: {cost_transport} грн")
    put_text(f"🏨 Вартість проживання ({days} днів): {cost_hotel} грн")

    put_markdown("---")
    put_text(f"Загальна сума: {total_cost} грн")

    if discount_summa:
        put_text(f"🎁 Знижка ({DISCOUNT_PERCENTAGE}%): -{discount_summa} грн")

    put_markdown(f"### 💰 ДО СПЛАТИ: {final_cost} грн")
