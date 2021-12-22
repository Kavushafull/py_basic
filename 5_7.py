txt_file = open("5_7.txt", "w", encoding="cp1251")
txt_list = ['Фирма-1 ООО 13000 7000\n', 'Фирма-2 АО 8000 1500\n', 'Фирма-3 ОАО 20000 25000\n', 'Фирма-4 ИП 2000 500\n']
txt_file.writelines(txt_list)
txt_file.close()

keys_profit = []
values_profit = []
keys_loses = []
values_loses = []
with open('5_7.txt') as txt_file:
    string = txt_file.readlines()
    for el in string:
        string_list = el.split(' ')
        if int(string_list[-2]) - int(string_list[-1]) > 0:
            keys_profit.append(string_list[0])
            values_profit.append(int(string_list[-2]) - int(string_list[-1]))
        else:
            keys_loses.append(string_list[0])
            values_loses.append(int(string_list[-1]) - int(string_list[-2]))
profit = dict(zip(keys_profit, values_profit))
avr_profit = dict(average_profit=sum(values_profit))
loses = dict(zip(keys_loses, values_loses))
avr_loses = dict(average_loses=sum(values_loses))
profit_list = [profit, avr_profit]
loses_list = [loses, avr_loses]
print(profit_list)
print(loses_list)

import json

with open('5_7.json', 'w') as json_file:
    json.dump(profit_list, json_file)
    json.dump(loses_list, json_file)
