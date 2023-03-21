# 1 задание
# Ввести с клавиатуры 4 строки и сохранить их  4 разные переменные
# Создать файл и записать в него первые 2 строки и закрыть файл
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки
# В итоговом файле должны быть 4 строки ,каждая должна начинаться с новой строки


# str1 = input("Введите строку №1:")
# str2 = input("Введите строку №2:")
# with open("file2.txt", "w", ) as file:
#     file.write(str1 + '\n')
#     file.write(str2 + '\n')
# str3 = input("Введите строку №3:")
# str4 = input("Введите строку №4:")
# with open("file2.txt", 'a') as file:
#     file.write(str3 + '\n')
#     file.write(str4)


# 2 задание
import json

data = {
    123456: ("Ivan", 25),
    654321: ("Petr", 35),
    987654: ("Marya", 29),
    345678: ("Ann", 32),
    567890: ("Dmitriy", 27)
}
with open('data.json', 'w') as file:
    json.dump(data, file)
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
print(loaded_data)

# 3 задание


import json
import csv

with open('data.json', 'r') as file:
    loaded_data = json.load(file)
table = [["ID", "Name", "Age", "Phone"]]
for id, info in data.items():
    table.append([id, info[0], info[1]])

# table[0].append("Phone")
table[1].append("222-1111")
table[2].append("444-2222")
table[3].append("222-3333")
table[4].append("333-4444")
table[5].append("111-5555")

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(table)
