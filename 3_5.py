def sum_el(a):
    b = []
    while 1 == 1:
        if a.count('end') == 0:
            a = a.split()
            for x in a:
                i = int(x)
                b.append(i)
            print(sum(b))
        else:
            a = a.split()
            for x in a[:a.index('end')]:
                i = int(x)
                b.append(i)
            break
        a = input('Введите числа через пробел либо введите end для окончания ')
    return sum(b)


a = input('Введите числа через пробел либо введите end для окончания ')
print(sum_el(a))
