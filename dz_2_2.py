word = input("Введите список элементов:")
a = list(word.split())
b = 0
for i in range(int(len(a) / 2)):
    a[b], a[b + 1] = a[b + 1], a[b]
    b += 2
print(a)
