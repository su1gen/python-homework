# Напишите определение класса с именем вооk. Класс Book должен иметь атрибуты данных
# для заголовка книги, имени автора и имени издателя. Этот класс должен также иметь
# следующие методы:
# • метод _ ini t _ () для класса должен принимать аргумент для каждого атрибута данных;
# • методы-получатели и методы-модификаторы для каждого атрибута данных;
# • метод _ str _ (), который возвращает строковое значение, сообщающее о состоянии
# объекта.


class Book:
    def __init__(self, title, author, publisher):
        self.__title = title
        self.__author = author
        self.__publisher = publisher

    def __str__(self):
        return f'{self.__title} {self.__author} {self.__publisher}'

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publisher(self):
        return self.__publisher

    def set_title(self, value):
        self.__title = value

    def set_author(self, value):
        self.__author = value

    def set_publisher(self, value):
        self.__publisher = value
