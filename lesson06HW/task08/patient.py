class Patient:
    def __init__(self, name, address, phone, contact):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__contact = contact

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_address(self):
        return self.__address

    def set_address(self, value):
        self.__address = value

    def get_phone(self):
        return self.__phone

    def set_phone(self, value):
        self.__phone = value

    def get_contact(self):
        return self.__contact

    def set_contact(self, value):
        self.__contact = value

    def __str__(self):
        return f'{self.__name} {self.__address} {self.__phone} {self.__contact}'