import json

class Employee:
    def __init__(self, name, id, department, position):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__position = position

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_id(self):
        return self.__id

    def set_id(self, value):
        self.__id = value

    def get_department(self):
        return self.__department

    def set_department(self, value):
        self.__department = value

    def get_position(self):
        return self.__position

    def set_position(self, value):
        self.__position = value

    def __str__(self):
        return f'{self.__name} {self.__id} {self.__department} {self.__position}'