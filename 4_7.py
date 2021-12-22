def fact(n):
    x = 1
    for el in range(1, int(n) + 1):
        x = x * el
        yield x

n = input('Введите число ')
for el in fact(n):
    print(el)