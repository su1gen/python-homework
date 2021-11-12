from lesson07HW.task05.person import Person


class Customer(Person):
    def __init__(self, name, address, phone, client_num, is_subscribed):
        super().__init__(name, address, phone)
        self.client_num = client_num
        self.is_subscribed = is_subscribed

    @property
    def client_num(self):
        return self.__client_num

    @client_num.setter
    def client_num(self, value):
        self.__client_num = value

    @property
    def is_subscribed(self):
        return self.__is_subscribed

    @is_subscribed.setter
    def is_subscribed(self, value):
        if value == '0':
            self.__is_subscribed = False
        else:
            self.__is_subscribed = True

    def __str__(self):
        return f'{super().__str__()} {self.__client_num} {self.__is_subscribed}'

