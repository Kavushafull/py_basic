import random as rd

list_1 = [rd.randint(0, 100) for x in range(15)]
print(list_1)
list_2 = []
for x in list_1[1:]:
    if x > list_1[list_1.index(x) - 1]:
        list_2.append(x)
    else:
        continue
print(list_2)
