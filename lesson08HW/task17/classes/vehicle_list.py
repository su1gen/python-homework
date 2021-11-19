from datetime import datetime

from lesson08HW.task17.classes.car import Car
from lesson08HW.task17.classes.plane import Plane
from lesson08HW.task17.classes.ship import Ship


class VehicleList:
    def __init__(self):
        self.__vehicles = list()

    def add(self, vehicle):
        self.__vehicles.append(vehicle)

    def get_avg_price(self):
        all_price = 0
        for vehicle in self.__vehicles:
            all_price += vehicle.price
        return round(all_price / len(self.__vehicles), 2)

    def get_max_speed(self):
        if len(self.__vehicles) > 0:
            max_speed = self.__vehicles[0].speed
            for vehicle in self.__vehicles:
                if vehicle.speed > max_speed:
                    max_speed = vehicle.speed
            return max_speed
        else:
            raise ValueError('List of vehicles is empty')

    def get_min_year(self):
        if len(self.__vehicles) > 0:
            min_year = self.__vehicles[0].year
            for vehicle in self.__vehicles:
                if vehicle.year < min_year:
                    min_year = vehicle.year
            return min_year
        else:
            raise ValueError('List of vehicles is empty')

    def get_most_expensive_vehicle(self):
        if len(self.__vehicles) > 0:
            most_expensive_vehicle = self.__vehicles[0]
            for vehicle in self.__vehicles:
                if vehicle.price > most_expensive_vehicle.price:
                    most_expensive_vehicle = vehicle
            return most_expensive_vehicle
        else:
            raise ValueError('List of vehicles is empty')

    def get_cheapest_vehicle(self):
        if len(self.__vehicles) > 0:
            cheapest_vehicle = self.__vehicles[0]
            for vehicle in self.__vehicles:
                if vehicle.price < cheapest_vehicle.price:
                    cheapest_vehicle = vehicle
            return cheapest_vehicle
        else:
            raise ValueError('List of vehicles is empty')

    def get_vehicles_cheaper_than_after_year(self, price, year):
        if len(self.__vehicles) > 0:
            result_vehicles = list()
            for vehicle in self.__vehicles:
                if vehicle.price < price and vehicle.year > year:
                    result_vehicles.append(vehicle)
            return result_vehicles
        else:
            raise ValueError('List of vehicles is empty')

    def get_vehicles_between_years(self, min_year, max_year):
        if len(self.__vehicles) > 0:
            result_vehicles = list()
            for vehicle in self.__vehicles:
                if min_year < vehicle.year < max_year:
                    result_vehicles.append(vehicle)
            return result_vehicles
        else:
            raise ValueError('List of vehicles is empty')

    def get_vehicles_not_older_average_price_between_speed(self, year, average_price, min_speed, max_speed):
        if len(self.__vehicles) > 0:
            result_vehicles = list()
            for vehicle in self.__vehicles:
                if datetime.now().year - vehicle.year <= year and \
                        (abs(vehicle.price - average_price) / vehicle.price) < 0.2 and \
                        min_speed < vehicle.speed < max_speed:
                    result_vehicles.append(vehicle)
            return result_vehicles
        else:
            raise ValueError('List of vehicles is empty')

    def get_amount_of_cars_and_planes(self):
        if len(self.__vehicles) > 0:
            amount = 0
            for vehicle in self.__vehicles:
                if isinstance(vehicle, Car) or isinstance(vehicle, Plane):
                    amount += 1
            return amount
        else:
            raise ValueError('List of vehicles is empty')

    def get_cheapest_car(self):
        if len(self.__vehicles) > 0:
            cheapest_car = self.__vehicles[0]
            for vehicle in self.__vehicles:
                if isinstance(vehicle, Car) and vehicle.price < cheapest_car.price:
                    cheapest_car = vehicle
            return cheapest_car
        else:
            raise ValueError('List of vehicles is empty')

    def get_ships_between_years(self, min_year, max_year):
        if len(self.__vehicles) > 0:
            result_vehicles = list()
            for vehicle in self.__vehicles:
                if isinstance(vehicle, Ship) and min_year < vehicle.year < max_year:
                    result_vehicles.append(vehicle)
            return result_vehicles
        else:
            raise ValueError('List of vehicles is empty')
