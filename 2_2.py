content = input('Введите содержимое через пробел ')
list1 = content.split(' ')
if len(list1)%2 == 0:
    list1[::2], list1[1::2] = list1[1::2], list1[::2]
else:
    list1[:-1:2], list1[1:-1:2] = list1[1:-1:2], list1[:-1:2]
print(list1)