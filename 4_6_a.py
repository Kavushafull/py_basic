from sys import argv
from itertools import count

script_name, number = argv

for x in count(int(number)):
    if x > 100:
        break
    else:
        print(x)
