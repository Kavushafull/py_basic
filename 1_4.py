a=1
number=int(input('Введите целое положительное число '))
while number > 0:
    b = number % 10
    if b >= a:
        a = b
    else:
        a = a
    number = number // 10
print('Самое большое число '+ str(a))