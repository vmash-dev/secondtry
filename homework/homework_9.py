car = {
    "model": "Toyota RAV4 Hybrid",
    "price": 1650000,
    "engine_volume": "2.5",
    "total_weight": 2225,
    "max_speed": 180,
    "fuel_consumption": 4.8,
    "interior_features": [
        "Мультимедійна система з 10.5-дюймовим дисплеєм",
        "Підігрів передніх сидінь",
        "Оздоблення керма шкірою",
        "Двозонний клімат-контроль"
    ],
    "luggage_capacity": {
        "standard": 580,
        "folded_seats": 1690
    }
}

car["max_trailer_weight"] = 1650

print(f"Назва авто: {car['model']}")
print(f"Ціна: {car['price']} грн")
print(f"Перша опція інтер'єру: {car['interior_features'][0]}")
print(f"Об'єм багажника зі складеними сидіннями: {car['luggage_capacity']['folded_seats']} л")

insurance_payment = car["price"] * 0.005
car["insurance"] = insurance_payment
print(f"Страховий платіж: {car['insurance']} грн")

fuel_price = 93
distance = 200
trip_cost = (car["fuel_consumption"] / 100) * distance * fuel_price

print(f"Вартість мандрівки на {distance} км: {trip_cost} грн")