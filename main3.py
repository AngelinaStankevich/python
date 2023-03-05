# #Задание 1
#
# name = input("Введите ваше имя:")
# age = int(input("Введите ваш возраст:"))
# # if age > 18:
# #     print(f'Приветсвую,{name}! У вас есть доступ к взрослому контенту.')
# # elif age < 18:
# #     print(f'Приветсвую,{name}! У вас нет доступа к взрослому контенту.')
# # else:
# #     print(f'Приветсвую,{name}! Поздравляю с совершеннолетием! У вас есть доступ к взрослому контенту.')
#
# if age >= 18:
#     print(f'Приветсвую,{name}! У вас есть доступ к взрослому контенту.')
#     if age == 18:
#         print(f'Приветсвую,{name}! Поздравляю с совершеннолетием! У вас есть доступ к взрослому контенту.')
# else:
#     print(f'Приветсвую,{name}! У вас нет доступа к взрослому контенту.')


#Задание 2

# str1 = input("Введите первую строку:")
# str2 = input("Введите вторую строку:")
# if set(str1) == set(str2):
#     print(True)
# else:
#     print(False)

#Задание 3

import random
options = ["камень", "ножницы","бумага"]
user_choice = input("Выберите камень, ножницы или бумага:")
bot_choice = random.choice(options)

if user_choice in options:
    if user_choice == bot_choice:
        print("Бот выбрал ту же опцию ")
        print("Ничья!")
    elif user_choice == "камень":
        if bot_choice == "ножницы":
            print("Бот выбрал ножницы ")
            print("Вы выиграли!")
        else:
            print("Бот выбрал бумагу ")
            print("Вы проиграли:(")
    elif user_choice == "бумага":
        if bot_choice == "ножницы":
            print("Бот выбрал ножницы ")
            print("Вы проиграли:(")
        else:
            print("Бот выбрал камень ")
            print("Вы выиграли!")
    elif user_choice == "ножницы":
        if bot_choice == "бумага":
            print("Бот выбрал бумагу ")
            print("Вы выиграли!")
        else:
            print("Бот выбрал камень ")
            print("Вы проиграли:(")
else:
    print("Вы выбрали неверную опцию ")

