import abc

class Vehicle(abc.ABC):
    def __init__(self, price, speed, year):
        self.price = price
        self.speed = speed
        self.year = year
        self.__latitude = None
        self.__longitude = None

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def get_coordinates(self):
        return self.__latitude, self.__longitude

    def set_coordinates(self, latitude, longitude):
        self.__latitude = latitude
        self.__longitude = longitude

    def __str__(self):
        return f'{self.price}, {self.speed}, {self.year}'




