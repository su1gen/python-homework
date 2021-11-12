from lesson07HW.task07.classes.book import Book


class BooksList:
    def __init__(self):
        self.__books = list()

    def add(self, book):
        self.__books.append(book)

    def get_books_by_author(self, author):
        return [book.__str__() for book in self.__books if author in book.authors]

    def get_books_by_publisher(self, publisher):
        return [book.__str__() for book in self.__books if book.publisher == publisher]

    def get_books_after_year(self, year):
        return [book.__str__() for book in self.__books if book.year >= year]

    def get_books_dict(self):
        return [book.to_dict() for book in self.__books]

    def get_books_from_dict(self, data):
        for book in data:
            self.__books.append(
                Book(book['id'], book['name'], book['authors'], book['publisher'], book['year'],
                         book['pages_amount'], book['price'], book['type']))





