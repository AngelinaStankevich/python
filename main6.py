#1 задание
# написать лямбда-функцию определяющую четное/нечетное.
# Функция принимает параметр(число) и если четное, то выдает слово "четное",если нет - то
# "нечетное"

# numbers = lambda *args: ["четное" if x % 2 == 0 else "нечетное" for x in args]
# print(*numbers(1, 4, 6, 8))

#2 задание
#Дан список чисел.Вернуть список ,где при помощи map() каждое число
#переведено в строку.В качестве функции map исподьзовать lambda

# numbers = [1, 4, 6, 7, 10]
# strings = list(map(lambda x: str(x), numbers))
# print(strings)

#3 задание
# При помощи функции filter() из кортежа слов отфильтровать только те,
# которые являются палиндромами (которые читаются одинакого в обе стороны)

# words = ('заказ', 'привет', 'топот', 'природа', 'шалаш')
# words1 = list(filter(lambda x: x == x[::-1], words))
# print(words1)

# 4 задание
# Написать декоратор к 2-м любым функциям , которые бы считал и выводил
# время их выполнения .Подсказка    from datetime import datetime
#                                   time = datetime.now()
#
# import time
#
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f'Время выполнения функции:{func.__name__}:{end_time - start_time}')
#         return result
#     return wrapper
#
# @timer
# def func1(num):
#     if num > 0:
#         print("Число больше 0")
#     elif num == 0:
#         print("Число равно 0")
#     else:
#         print("Число меньше 0")
#
#
# @timer
# def func2(a, b):
#     return a ^ b
#
#
# func1(9)
# func2(2, 4)



