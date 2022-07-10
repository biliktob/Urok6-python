import time
class TrafficLight():
    def __init__(self, color):
        self.__color = color
    def running(self):
        while True:
            if self.__color == 'red':
                print('Горит красный')
                time.sleep(7)
                print('Горит желтый')
                time.sleep(2)
                print('Горит зеленый')
                time.sleep(3)
            if self.__color == 'yellow':
                print('Горит желтый')
                time.sleep(2)
                print('Горит зеленый')
                time.sleep(3)
                print('Горит красный')
                time.sleep(7)
            if self.__color == 'green':
                print('Горит зеленый')
                time.sleep(3)
                print('Горит красный')
                time.sleep(7)
                print('Горит желтый')
                time.sleep(2)
traffic_light = TrafficLight('yellow')
traffic_light.running()
