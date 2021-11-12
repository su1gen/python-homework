# 5. Book: id, Название, Автор (ы), Издательство, Год издания, Количество страниц, Цена, Тип переплета.
# Создать массив объектов.
# Вывести:
# a) список книг заданного автора;
# b) список книг, выпущенных заданным издательством;
# c) список книг, выпущенных после заданного года.
from lesson07HW.task07.classes.book import Book
from lesson07HW.task07.classes.books_list import BooksList

if __name__ == '__main__':
    b1 = Book(1, 'first', ['first1', 'first2'], 'first', 1999, 300, 100, 'first')
    b2 = Book(2, 'second', ['second1', 'second2'], 'second', 1966, 200, 100, 'second')
    b3 = Book(3, 'third', ['first1', 'third2'], 'first', 1922, 300, 100, 'third')

    books_list = BooksList()

    books_list.add(b1)
    books_list.add(b2)
    books_list.add(b3)

    print(books_list.get_books_by_author('first1'))
    print(books_list.get_books_by_publisher('second'))
    print(books_list.get_books_after_year(1966))
