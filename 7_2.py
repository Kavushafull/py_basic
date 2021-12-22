class Clothes:
    fabrics = 0

    def jakets_sum(self, size, count=1):
        self.fabrics = self.fabrics + ((size / 6.5) + 0.5) * count
        return ((size / 6.5) + 0.5) * count

    def suits_sum(self, height, count=1):
        self.fabrics = self.fabrics + ((height * 2) + 0.3) * count
        return ((height * 2) + 0.3) * count

    @property
    def fabrics_sum(self):
        return f'Ткани требуется {self.fabrics}'


a = Clothes()
print(a.jakets_sum(5, 4))
print(a.suits_sum(6, 1))
print(a.fabrics_sum)
print(a.suits_sum(4, 1))
print(a.fabrics_sum)
