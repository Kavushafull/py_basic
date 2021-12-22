distance = int(input('Дистанция за первый день '))
goal = int(input('Введите цель '))
day = 1
while distance < goal:
    distance = distance + (distance * 0.1)
    day = day + 1
print(f'Цель будет достигнута на {day} день')