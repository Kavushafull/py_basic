def exp_1(x, y):
    if int(y) != 0:
        x = float('.'.join(x.split(',')))
        y = abs(int(y))
        return 1 / (x ** y)
    else:
        x = 1
        return 1


def exp_2(x, y):
    if int(y) != 0:
        x = float('.'.join(x.split(',')))
        y = abs(int(y))
        i = 0
        z = 1
        for i in range(y):
            i = i + 1
            z = z * x
        return 1 / z
    else:
        return 1


x = input('Введите число ')
y = input('Введите степень ')
print(exp_1(x, y))
print(exp_2(x, y))
