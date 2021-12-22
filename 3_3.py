def max_sum(x, y, z):
    my_list = []
    my_list.append(int(x))
    my_list.append(int(y))
    my_list.append(int(z))
    my_list.sort()
    return my_list[-1] + my_list[-2]


x = input('x=')
y = input('y=')
z = input('z=')
print(max_sum(x, y, z))
