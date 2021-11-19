from lesson08HW.task17.classes.flyable import Flyable
from lesson08HW.task17.classes.vehicle import Vehicle


class Plane(Vehicle, Flyable):
    def __init__(self, price, speed, year, height, passengers):
        super().__init__(price, speed, year)
        self.height = height
        self.passengers = passengers

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, value):
        self.__passengers = value

    def __str__(self):
        return f'{super().__str__()}, {self.height}, {self.passengers}'