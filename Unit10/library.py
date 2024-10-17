import csv

class Book:
    __slots__ = ["author", "title", "copies"]
    def __init__(self, title, author, copies):
        self.title=title
        self.author = author
        self.copies=copies

class Patron:
    __slots__ = ["id", "name", "want_list", "checked_out_books"]
    def __init__(self, id, name):
        self.id = id
        self.name=name
        self.want_list= set()
        self.checked_out_books= set()

class CardCatalog:
    __slots__ = ["books_by_title", "books_by_author"]
    def __init__(self):
        self.books_by_title = {}
        self.books_by_author = {}


class Library:
    __slots__ = ["shelves", "card_catalog", "patrons"]
    def __init__(self, books):
        self.shelves = set(books)
        self.card_catalog = CardCatalog()

        titles = self.card_catalog.books_by_title
        authors = self.card_catalog.books_by_author

        for book in books:
            title = book.title
            add_to_catalog (title, book, title)

            author = book.author
            add_to_catalog(author, book, authors)


        self.patrons = {} 

def add_to_catalog(key, book, dictionary):
    if key not in dictionary:
        dictionary[key] = set()
    books = dictionary[key]
    books.add(book)

def read_books(filename):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(file)
        books = set()
        for record in csv_reader:
            title = record[0]
            author = record[1]
            copies = int(record[2])
            book = Book(title, author, copies)
            books.add(book)
        return books




def main():
    books = read_books("data/books.csv")

    library = Library(books)
    print(library.card_catalog.books_by_author)


if __name__ == "__main__":
    main()


    