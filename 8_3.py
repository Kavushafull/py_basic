class NotNumber(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return f'Невозможно выполнить операцию: {self.error}'


numbers_list = []
while True:
    numbers_str = input()
    numbers = numbers_str.split(' ')
    if 'stop' in numbers:
        for x in numbers[:numbers.index('stop')]:
            try:
                if x.isdigit():
                    numbers_list.append(x)
                else:
                    raise NotNumber(f'{x} не является цифрой!')
            except NotNumber as ntn:
                print(ntn)
        print(numbers_list)
        print('Скрипт завершен!')
        break
    else:
        for x in numbers:
            try:
                if x.isdigit():
                    numbers_list.append(x)
                else:
                    raise NotNumber(f'{x} не является цифрой!')
            except NotNumber as ntn:
                print(ntn)
