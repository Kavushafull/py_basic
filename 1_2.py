seconds = int(input('Введите колличество секунд '))
print(f'{seconds//3600:02d}:{(seconds%3600)//60:02d}:{seconds%60:02d}')