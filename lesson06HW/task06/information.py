class Information:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_address(self):
        return self.__address

    def set_address(self, value):
        self.__address = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

    def get_phone(self):
        return self.__phone

    def set_phone(self, value):
        self.__phone = value