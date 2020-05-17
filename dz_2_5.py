my_list = [7, 5, 3, 3, 2]
while True:
    rating = input('Введите новое значение рейтинга: ')
    try:
        rating = abs(int(rating))
    except ValueError as eror:
        print('Ошибка ввода')
        continue
    if not my_list.count(rating):
        if rating > my_list[0]:
            my_list.insert(0, rating)
        elif rating < my_list[-1]:
            my_list.append(rating)
        else:
            for k, v in enumerate(my_list):
                if rating > v:
                    my_list.insert(k, rating)
                    break
    else:
        new_index = my_list.index(rating) + my_list.count(rating)
        my_list.insert(new_index, rating)
    print(my_list)
