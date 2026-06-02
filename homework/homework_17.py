class Car:
    def __init__(self, model: str, age: int, owner: str = "", fuel: float = 0):
        self.model = model.title().strip()
        self.age = age
        self.owner = owner
        self.fuel = fuel
        self.car_id = id(self)

    def __str__(self) -> str:
        return f"Років машині: {self.model}, {self.age}, власник: {self.owner or 'немає'}, бенз: {self.fuel} літрів"

    def refuel(self, amount: float):
        self.fuel += amount

    @property
    def state(self) -> str:
        if self.age <= 4:
            return "Нове авто"
        elif 5 <= self.age <= 10:
            return "Середній стан"
        else:
            return "Старе авто"

    @property
    def fuel_status(self) -> str:
        if self.fuel < 5:
            return "Заправся"
        elif 5 <= self.fuel < 20:
            return "Норм"
        else:
            return "Куди захочеш поїду"


car_1 = Car(model="Toyota RAV4", age=1, owner="Shinshila")
car_2 = Car(model="Honda CR-V", age=4)

print(id(car_1))

print(id(car_2))

print(car_1.__dict__)

print(car_2.__dict__)

print(car_1)

print(car_2)

car_1.fuel += 5

print(car_1)

car_2.refuel(20)

print(car_2)

print(car_1.state)

print(car_2.state)

if car_1.fuel > car_2.fuel:
    print(f"Більше бензину у {car_1.model}")
else:
    print(f"Більше бензину у {car_2.model}")

print(car_1.fuel_status)
print(car_2.fuel_status)
