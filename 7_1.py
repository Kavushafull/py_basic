class Matrix:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __add__(self, other):
        return Matrix(
            [self.list_of_list[0] + other.list_of_list[0], self.list_of_list[1] + other.list_of_list[1],
             self.list_of_list[2] + other.list_of_list[2], self.list_of_list[3] + other.list_of_list[3]])

    def __str__(self):
        return f'{self.list_of_list[0]} {self.list_of_list[1]}\n' f'{self.list_of_list[2]} {self.list_of_list[3]}\n'


a_1 = Matrix([1, 2, 3, 4])
print(a_1)
a_2 = Matrix([5, 6, 7, 8])
print(a_2)
print(a_1 + a_2)
