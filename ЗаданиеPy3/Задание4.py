class Car:
    manufacturer: str = "Unknown"
    wheels: int = 4

    def __init__(self, model: str, year: int, color: str, mileage: float, price: float) -> None:
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.price = price

    def drive(self, distance: float) -> None:
        if distance > 0:
            self.mileage += distance
            print(f"{self.model} проехал {distance} км. Новый пробег: {self.mileage} км.")
        else:
            print("Расстояние должно быть положительным.")

    def repaint(self, new_color: str) -> None:
        self.color = new_color
        print(f"{self.model} теперь {self.color}.")

    def apply_discount(self, discount_percentage: float) -> None:
        if 0 <= discount_percentage <= 100:
            discount_amount = (discount_percentage / 100) * self.price
            self.price -= discount_amount
            print(f"Цена {self.model} после скидки: {self.price:.2f}.")
        else:
            print("Скидка должна быть в диапазоне от 0 до 100.")

    def __str__(self) -> str:
        return f"{self.year} {self.color} {self.model}, пробег: {self.mileage} км, цена: {self.price:.2f}"

car1 = Car(model="Toyota Camry", year=2020, color="черный", mileage=15000.0, price=25000.0)
car2 = Car(model="Honda Accord", year=2019, color="белый", mileage=30000.0, price=23000.0)

print(car1)
car1.drive(100)
car1.repaint("синий")
car1.apply_discount(10)

print(car2)
car2.drive(200)
car2.apply_discount(5)
