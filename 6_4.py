class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.color} {self.name} поехала')

    def stop(self):
        print(f'Машина {self.color} {self.name} остановилась')

    def show_speed(self):
        print(f'Скорость движения {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышена скорость!')
        else:
            print(f'Скорость движения {self.speed}')


class SportCar(Car):
    def sport_car(self):
        if self.is_police == False:
            print('Sport Car')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышена скорость!')
        else:
            print(f'Скорость движения {self.speed}')


class PoliceCar(Car):
    def police_car(self):
        if self.is_police == True:
            print('Police Car')


car_1 = Car(70, 'green', 'toyota')
car_1.go()
car_1.stop()
car_1.show_speed()

car_2 = TownCar(70, 'red', 'gelly')
car_2.go()
car_2.stop()
car_2.show_speed()

car_3 = SportCar(100, 'blue', 'aston martin')
car_3.go()
car_3.stop()
car_3.show_speed()
car_3.sport_car()

car_4 = WorkCar(35, 'yellow', 'skoda')
car_4.go()
car_4.stop()
car_4.show_speed()

car_5 = PoliceCar(85, 'white-blue', 'dodge', True)
car_5.go()
car_5.stop()
car_5.show_speed()
car_5.police_car()
