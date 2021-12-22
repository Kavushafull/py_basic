def UpFirst(x):
    x = x.split()
    y = []
    for i in x:
        y.append(i[0:1].upper() + i[1:].lower())
    return ' '.join(y)


text = input('Введите текст: ')
print(UpFirst(text))