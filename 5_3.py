txt_file = open("5_3.txt", "w", encoding="cp1251")
text_list = ['Петров — 100000\n', 'Зиновьев — 62000\n', 'Гришин — 13000\n', 'Иванов — 40000\n', 'Сидоров — 19000\n']
txt_file.writelines(text_list)
txt_file.close()

txt_file = open("5_3.txt", "r", encoding="cp1251")
text_list = txt_file.readlines()
low_salary = []
salary = []
for x in text_list:
    print(x)
    employee = x.split(' ')
    salary.append(int(employee[-1]))
    if int(employee[-1]) < 20000:
        low_salary.append(employee[0])
    else:
        continue
for x in low_salary:
    print('Зарплата ниже 20000 ', x)
print('средняя зарплата ', sum(salary) / len(salary))
