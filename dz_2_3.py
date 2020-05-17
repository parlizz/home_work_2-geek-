i = int(input("Введите число от 1 до 12:"))

seasons = {'Зима': (12, 1, 2),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)
           }
for key in seasons.keys():
    if i in seasons[key]:
        print(key)
