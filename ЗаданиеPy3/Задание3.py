from typing import Literal, Any, Union

def function_name(
        search: Literal["args", "kwargs"],
        status: bool,
        *args: Any,
        **kwargs: Any
) -> Union[list[int], str]:
    """
        Функция для обработки аргументов и ключевых аргументов в зависимости от параметров 'search' и 'status'.

        Аргументы:
        search (Literal["args", "kwargs"]): Определяет тип поиска (аргументы или ключевые аргументы).
        status (bool): Определяет режим обработки аргументов (истина - вернуть список целых чисел, ложь - объединить аргументы в строку).
        *args (Any): Аргументы переменной длины.
        **kwargs (Any): Ключевые аргументы переменной длины.

        Возвращает:
        Union[list[int], str]: Возвращает список целых чисел или строку в зависимости от параметров 'search' и 'status'.
        """
    result: list[int] = []
    result_2: str = ""
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += f"Key: {k}, Value: {v}; "
        return result_2
    else:
        raise ValueError("Error for search")
