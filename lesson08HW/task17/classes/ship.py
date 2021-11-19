from lesson08HW.task17.classes.swimable import Swimable
from lesson08HW.task17.classes.vehicle import Vehicle


class Ship(Vehicle, Swimable):
    def __init__(self, price, speed, year, passengers, port):
        super().__init__(price, speed, year)
        self.passengers = passengers
        self.port = port

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, value):
        self.__passengers = value

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        self.__port = value

    def __str__(self):
        return f'{super().__str__()}, {self.passengers}, {self.port}'
