def div_el(x, y):
    if y == 0:
        return 'На ноль делить нельзя!'
    else:
        return int(x) / int(y)


x = input('Введите делимое ')
y = input('Введите делитель ')
print(div_el(x, y))
