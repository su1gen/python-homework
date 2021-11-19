from lesson08HW.task17.classes.car import Car
from lesson08HW.task17.classes.swimable import Swimable


class Amfibia(Car, Swimable):
    def __init__(self, price, speed, year):
        super().__init__(price, speed, year)