class ComplexNumbers:
    def __init__(self, z):
        self.z = z.split()

    def __add__(self, other):
        b = str(''.join(x for x in self.z if 'i' in x))
        d = str(''.join(x for x in other.z if 'i' in x))
        poz_b = int(''.join(str(self.z.index(x)) for x in self.z if 'i' in x))
        poz_d = int(''.join(str(other.z.index(x)) for x in other.z if 'i' in x))
        if len(b) == 1 and len(d) == 1:
            return f'z = {int(self.z[2 - poz_b]) + int(other.z[2 - poz_d])}'
        elif len(b) == 1 and len(d) != 1:
            return f'z = {int(self.z[2 - poz_b]) + int(other.z[2 - poz_d])} + {other.z[poz_d]}i'
        elif len(b) != 1 and len(d) == 1:
            return f'z = {int(self.z[2 - poz_b]) + int(other.z[2 - poz_d])} + {self.z[poz_b]}i'
        else:
            return f'z = {int(self.z[2 - poz_b]) + int(other.z[2 - poz_d])} + {int(b[:-1]) + int(d[:-1])}i'

    def __mul__(self, other):
        b = str(''.join(x for x in self.z if 'i' in x))
        d = str(''.join(x for x in other.z if 'i' in x))
        poz_b = int(''.join(str(self.z.index(x)) for x in self.z if 'i' in x))
        poz_d = int(''.join(str(other.z.index(x)) for x in other.z if 'i' in x))
        if len(b) == 1 and len(d) == 1:
            return f'z = {int(self.z[2 - poz_b]) * int(other.z[2 - poz_d])}'
        elif len(b) == 1 and len(d) != 1:
            return f'z = {int(self.z[2 - poz_b]) * int(other.z[2 - poz_d])} + {int(self.z[2 - poz_b]) * int(d[:-1])}i'
        elif len(b) != 1 and len(d) == 1:
            return f'z = {int(self.z[2 - poz_b]) * int(other.z[2 - poz_d])} + {int(other.z[2 - poz_d]) * int(b[:-1])}i'
        else:
            return f'z = {(int(self.z[2 - poz_b]) * int(other.z[2 - poz_d])) - (int(b[:-1]) * int(d[:-1]))} + {(int(self.z[2 - poz_b]) * int(d[:-1])) + (int(other.z[2 - poz_d]) * int(b[:-1]))}i'


z1 = ComplexNumbers('13 + 4i')
z2 = ComplexNumbers('6 + 2i')
print(z1 * z2)
