class ZeroDivision(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return f'Невозможно выполнить операцию: {self.error}'


a = float(input())
b = float(input())
try:
    if b == 0:
        raise ZeroDivision('Делить на ноль нельзя!')
    print(a / b)
except ZeroDivision as err:
    print(err)
finally:
    print('Программа завершена')
