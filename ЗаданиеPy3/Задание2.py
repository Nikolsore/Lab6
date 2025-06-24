import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b, mode='full'):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль!")
    if mode == 'full':
        return a / b
    elif mode == 'remainder':
        return a % b
    elif mode == 'integer':
        return a // b


def power(a, b):
    return a ** b


def factorial(n):
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def sqrt(a):
    if a < 0:
        raise ValueError("Квадратный корень.")
    return math.sqrt(a)



def main():
    operations = {
        "1": {"name": "Сложение", "func": lambda a, b: add(a, b)},
        "2": {"name": "Вычитание", "func": lambda a, b: subtract(a, b)},
        "3": {"name": "Умножение", "func": lambda a, b: multiply(a, b)},
        "4": {"name": "Деление", "func": lambda a, b, m: divide(a, b, m)},
        "5": {"name": "Возведение в степень", "func": lambda a, b: power(a, b)},
        "6": {"name": "Факториал", "func": lambda n: factorial(n)},
        "7": {"name": "Квадратный корень", "func": lambda a: sqrt(a)},
    }

    while True:
        print("\nМеню калькулятора:")
        for key, value in operations.items():
            print(f"{key}. {value['name']}")
        print("exit для выхода")

        choice = input("Выберите операцию: ")

        if choice.lower() == 'exit':
            break

        if choice not in operations:
            print("Недопустимый выбор. Пожалуйста, выберите номер операции или введите 'exit'.")
            continue

        try:
            if choice == "4":
                a = float(input("Введите делимое: "))
                b = float(input("Введите делитель: "))
                mode = input("Выберите деления (full, remainder, integer): ")
                print(f"{a} {mode} {b} = {operations[choice]['func'](a, b, mode)}")
            elif choice == "6":
                n = int(input("Введите число для вычисления факториала: "))
                print(f"Факториал {n} = {operations[choice]['func'](n)}")
            elif choice == "7":
                a = float(input("Введите число для вычисления квадратного корня: "))
                print(f"Квадратный корень из {a} = {operations[choice]['func'](a)}")
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                print(f"{a} {operations[choice]['name']} {b} = {operations[choice]['func'](a, b)}")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
