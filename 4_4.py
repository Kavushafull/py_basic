import random as rd

list_1 = [rd.randint(0, 10) for x in range(15)]
print(list_1)
list_2 = []
for x in list_1:
    if list_2.count(x) == 0:
        list_2.append(x)
    else:
        continue
print(list_2)
