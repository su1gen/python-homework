class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name

    def set_animal_type(self, value):
        self.__animal_type = value

    def get_animal_type(self):
        return self.__animal_type

    def set_age(self, value):
        self.__age = value

    def get_age(self):
        return self.__age