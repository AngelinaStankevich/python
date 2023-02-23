#1.1 задание

a = 100
b = 100
c = 100
print(id(a))
print(id(b))
print(id(c))


#1.2 задание

num1 = [0, 1, 2]
num2 = [0, 1, 2]
print(id(num1))
print(id(num2))


#2 задание

a = 1
b = 2
c = 3
a, b = b, a
print(f'{a}, {b}, {c}')
b, c = c, b
print(f'{a}, {b}, {c}')


#3 задание

countries_capitals = {'Belarus': 'Minsk', 'Poland': 'Warsaw', 'Great Britain': 'London'}
print(countries_capitals['Poland'])
print(countries_capitals['Belarus'])


#4 задание

food = ['котлета', 'пюрешка', 'драники', 'пицца', 'мороженное']
print('Из предложенного я больше люблю', food[3], 'и', food[4])


#5 задание

friends = ['Egor', 'Liza', 'Vanya', 'Yana']
print('Введите имя:')
name = str(input())
if name in friends:
    print('У меня есть друг с именем', name)
else:
    print('У меня нет друга с именем', name)











