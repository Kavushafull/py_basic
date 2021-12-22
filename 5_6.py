txt_file = open("5_6.txt", "w", encoding="cp1251")
txt_list = ['Информатика: 100(л) 50(пр) 20(лаб).\n', 'Физика: 30(л) — 10(лаб)\n', 'Физкультура: — 30(пр) —\n']
txt_file.writelines(txt_list)
txt_file.close()

txt_file = open("5_6.txt", "r", encoding="cp1251")
string = txt_file.readlines()
keys = []
values = []
for el in string:
    string_list = el.split(' ')
    keys.append((string_list[0])[0:-1])
    numbers = []
    for x in string_list[1:]:
        y = ''
        for i in x:
            if i.isdigit():
                y = y + i
            else:
                continue
        if y == '':
            continue
        else:
            numbers.append(y)
    values.append(sum(int(n) for n in numbers))
classes_dict = dict(zip(keys, values))
print(classes_dict)
txt_file.close()
