# Написать декоратор, который будет выводить в консоль
# имя функции, время вызова, и с какими параметрами она вызвана
# Примеры работы:
# add(1, 2) -> Функция add вызвана в 2023-03-14 22:21:53.986665 с позиционными параметрами (1, 2)
# add(a=1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986703 с именнованными параметрами {'a': 1, 'b': 2}
# add(1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986718 с позиционными параметрами (1,) и с именнованными параметрами {'b': 2}

# Дополнительно (если есть время) добавить код для обработки такого примера:
# add() -> Функция add вызвана в 2023-03-14 22:25:46.942232 без параметров

import datetime
from typing import Callable


def log_function_call(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        now_time = datetime.datetime.now()
        positional_args = ", ".join(str(arg) for arg in args)
        keyword_args = ", ".join(f"{k}={v}" for k, v in kwargs.items())

        if args and kwargs:
            print(f"Function {func.__name__} called at {now_time} with positional arguments: {positional_args} and keyword arguments: {keyword_args}")
        elif kwargs and args:
            print(f"Function {func.__name__} called at {now_time} with positional arguments: {keyword_args} and keyword arguments: {positional_args}")
        elif args:
            print(f"Function {func.__name__} called at {now_time} with positional arguments: {positional_args}")
        elif kwargs:
            print(f"Function {func.__name__} called at {now_time} with keyword arguments: {keyword_args}")
        return func(*args, **kwargs)
    return inner



@log_function_call
def add(a: int, b: int) -> int:
    return a + b


add(a = 5, b = 5)
