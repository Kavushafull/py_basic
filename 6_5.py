class Stationery:
    title = 'Parker'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки с помощью ручки.')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки с помощью карандаша.')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки с помощью маркера.')


el_1 = Stationery()
el_1.draw()
print(el_1.title)

el_2 = Pen()
el_2.draw()
print(el_2.title)

el_3 = Pencil()
el_3.draw()
print(el_3.title)

el_4 = Handle()
el_4.draw()
print(el_4.title)
