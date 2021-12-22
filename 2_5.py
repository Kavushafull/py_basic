my_list = [7, 5, 3, 3, 2]
number = int(input('Введите число '))
for x in my_list:
    if number > x:
        my_list.insert(my_list.index(x), number)
        break
    elif number < my_list[-1]:
        my_list.append(number)
        break
    else:
        continue
print(my_list)