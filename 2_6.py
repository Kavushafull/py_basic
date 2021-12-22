keys_list = ['название', 'цена', 'количество', 'единицы измерения']
x = 0
names = []
prices = []
numbers = []
units = []
goods_struct = []
for x in range(3):
    good = input('Введите название, цену, количество и еденицы имерения товара через пробел: ')
    good_list = good.split(' ')
    good_dict = dict(zip(keys_list, good_list))
    struct = [x + 1]
    struct.append(good_dict)
    goods_struct.append(tuple(struct))
    names.append(good_dict.get('название'))
    prices.append(good_dict.get('цена'))
    numbers.append(good_dict.get('количество'))
    units.append(good_dict.get('единицы измерения'))
goods_list = [names, prices, numbers, units]
goods_dict = dict(zip(keys_list, goods_list))
print(goods_struct)
print(goods_dict)
