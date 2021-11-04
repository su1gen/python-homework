class RetailItem:
    def __init__(self, description, amount, price):
        self.__description = description
        self.__amount = amount
        self.__price = price

    def get_description(self):
        return self.__description

    def set_description(self, value):
        self.__description = value

    def get_amount(self):
        return self.__amount

    def set_amount(self, value):
        self.__amount = value

    def get_price(self):
        return self.__price

    def set_price(self, value):
        self.__price = value

    def __str__(self):
        return f'{self.__description} {self.__amount} {self.__price}'