import library

def test_construct_book():
    title = "Holly"
    author = "Stephen King"
    copies = 7

    book = library.Book(title, author, copies)

    assert title == book.title
    assert author == book.author
    assert copies == book.copies

def test_contruct_patron():
    id = "ABC1234"
    name = "Todd"
    empty_set = set()

    patron = library.Patron(id, name)

    assert id == patron.id
    assert name == patron.name
    assert empty_set == patron.want_list
    assert empty_set == patron.checked_out_books

def test_contruct_cardcatalog():
    empty_dict = {}

    catalog = library.CardCatalog()
    assert empty_dict == catalog.books_by_title
    assert empty_dict == catalog.books_by_author