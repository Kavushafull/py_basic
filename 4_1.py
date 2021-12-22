from sys import argv

script_name, hours, salary, bonus = argv

print('Итоговая зарплата ', (float(hours) * float(salary)) + (float(hours) * float(salary) * (float(bonus) / 100)))
