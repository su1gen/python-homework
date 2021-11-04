class Procedure:
    def __init__(self, name, date, doctor, price):
        self.__name = name
        self.__date = date
        self.__doctor = doctor
        self.__price = price

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_date(self):
        return self.__date

    def set_date(self, value):
        self.__date = value

    def get_doctor(self):
        return self.__doctor

    def set_doctor(self, value):
        self.__doctor = value

    def get_price(self):
        return self.__price

    def set_price(self, value):
        self.__price = value

    def __str__(self):
        return f'{self.__name} {self.__date} {self.__doctor} {self.__price}'