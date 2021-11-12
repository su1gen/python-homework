class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    def __str__(self):
        return f'{self.__name} {self.__number}'

