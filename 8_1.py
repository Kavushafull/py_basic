class Date:
    day = 0
    month = 0
    year = 0

    @classmethod
    def str_to_int(cls, date):
        date_list = date.split('-')
        cls.day = date_list[0]
        cls.month = date_list[1]
        cls.year = date_list[2]

    @staticmethod
    def validation(date):
        months = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30,
                  '12': 31}
        date = date.split('-')
        if not (13 > int(date[1]) > 0):
            return 'Неверное значение месяца'
        elif not (1900 < int(date[2]) < 2021):
            return 'Выход за временной диапалон'
        elif not (0 < int(date[0]) <= months.get(date[1])):
            return 'Неверное колличество дней месяца'
        else:
            return 'Данные верны'


Date.str_to_int('21-10-2002')
print(Date.day)
print(Date.month)
print(Date.year)
print(Date.validation('25-9-1902'))
