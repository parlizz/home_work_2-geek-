list_words = [str(i) for i in input('Введите строку: ').split()]
i = 1
for word in list_words:
    print(f'№{i}: {word[0:10:1]}')
    i += 1
