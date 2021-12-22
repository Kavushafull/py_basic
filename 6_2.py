class Road:
    def AsphMass(self, _length, _width, _thickness):
        mass = _length * _width * (25 * _thickness)
        return f'Расход асфальта {mass} кг'


a = Road()
print(a.AsphMass(100, 2, 4))
