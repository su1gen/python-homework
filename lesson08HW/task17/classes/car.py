from lesson08HW.task17.classes.movable import Movable
from lesson08HW.task17.classes.vehicle import Vehicle


class Car(Vehicle, Movable):
    def __init__(self, price, speed, year):
        super().__init__(price, speed, year)