class Human:
    def __init__(self, id, surname, name, patronymic, address, phone):
        self.id = id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.address = address
        self.phone = phone

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value):
        self.__patronymic = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    def __str__(self):
        return f'{self.__id}, {self.__surname}, {self.__name}, {self.__patronymic}, {self.__address}'

    def to_dict(self):
        human_dict = dict()
        human_dict["id"] = self.__id
        human_dict["surname"] = self.__surname
        human_dict["name"] = self.__name
        human_dict["patronymic"] = self.__patronymic
        human_dict["address"] = self.__address
        human_dict["phone"] = self.__phone
        return human_dict
    