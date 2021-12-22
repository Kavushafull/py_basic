import time


class TrafficLight:
    __color = 0

    def running(self):
        i = 0
        while i < 2:
            list_1 = []
            for x in range(3):
                if x == 0:
                    __color = 'red'
                    print(__color)
                    list_1.append(__color)
                    time.sleep(7)
                elif x == 1:
                    __color = 'yellow'
                    print(__color)
                    list_1.append(__color)
                    time.sleep(2)
                else:
                    __color = 'green'
                    print(__color)
                    list_1.append(__color)
                    time.sleep(16)
            if list_1[0] != 'red' or list_1[1] != 'yellow' or list_1[2] != 'green':
                print('ERROR!')
                break
            else:
                i += 1


a = TrafficLight()
print(a._TrafficLight__color)
a.running()
