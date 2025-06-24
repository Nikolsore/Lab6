from typing import TypeVar, Callable

N = TypeVar('N', int, float, str)


def multiply_list(elements: list[N], multiplier: int | float = 2) -> list[N]:
    return [element * multiplier for element in elements]


multiply_lambda: Callable[[list[N], int | float], list[N]] = lambda elements, multiplier=2: list(
    map(lambda x: x * multiplier, elements))

# числа
numbers = [1, 2, 3]
print(multiply_list(numbers, 3))  # [3, 6, 9]
print(multiply_lambda(numbers, 3))  # [3, 6, 9]

# множитель по умолчанию
print(multiply_list(numbers))  # [2, 4, 6]
print(multiply_lambda(numbers))  # [2, 4, 6]

# строки
strings = ['w', 'l']
print(multiply_list(strings, 3))  # ['www', 'lll']
print(multiply_lambda(strings, 3))  # ['www', 'lll']
