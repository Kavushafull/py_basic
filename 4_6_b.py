from sys import argv
from itertools import cycle

script_name, number = argv

i = 0
for x in cycle(number):
    if i > 10:
        break
    else:
        print(x)
        i += 1
