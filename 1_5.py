income = int(input('Введите Ваши доходы '))
expenses = int(input('Введите Ваши расходы '))
if income > expenses:
    print(f'Ваша прибыль составляет {income-expenses}')
    print(f'Рентабельность {((income-expenses)/income)*100} процентов')
    staff = int(input('Введите число сотрудников '))
    print(f'Прибыль на одного сотрудника {(income-expenses)/staff}')
elif income == expenses:
    print('Вы работаете в 0')
else:
    print(f'Ваш убыток составляет {expenses-income}')