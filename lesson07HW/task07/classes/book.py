class Book:
    def __init__(self, id, name, authors, publisher, year, pages_amount, price, type):
        self.id = id
        self.name = name
        self.authors = authors
        self.publisher = publisher
        self.year = year
        self.pages_amount = pages_amount
        self.price = price
        self.type = type

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        self.__authors = value

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, value):
        self.__publisher = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def pages_amount(self):
        return self.__pages_amount

    @pages_amount.setter
    def pages_amount(self, value):
        self.__pages_amount = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    def __str__(self):
        return f'{self.__id}, {self.__name}, {self.__authors}, {self.__publisher}, {self.__year}, {self.__pages_amount}, {self.__price}, {self.__type}'

    def to_dict(self):
        human_dict = dict()
        human_dict["id"] = self.__id
        human_dict["name"] = self.__name
        human_dict["authors"] = self.__authors
        human_dict["publisher"] = self.__publisher
        human_dict["year"] = self.__year
        human_dict["pages_amount"] = self.__pages_amount
        human_dict["price"] = self.__price
        human_dict["type"] = self.__type
        return human_dict
