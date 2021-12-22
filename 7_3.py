class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        if self.count > other.count:
            return self.count - other.count
        elif self.count < other.count:
            return other.count - self.count
        else:
            return 'Количество ячеек клеток равно!'

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        if self.count > other.count:
            return self.count // other.count
        else:
            return other.count // self.count

    def make_order(self, number):
        list_of_cells = []
        for i in range(self.count):
            list_of_cells.append('*')
        for i in reversed(range(self.count // number)):
            list_of_cells.insert((i + 1) * number, '\n')
        return ''.join(list_of_cells)


a = Cell(5)
print(a.count)
b = Cell(2)
print(b.count)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(2))
