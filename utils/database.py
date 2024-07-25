books = []
BOOK_INFO = ('name', 'author', 'read')


def add_book(name, author):
    book_data = (name, author, False)
    book = dict(zip(BOOK_INFO, book_data))
    books.append(book)


def list_book():
    for book in books:
        print('-' * 10)
        for key, value in book.items():
            print(f"{key}: {value}")


def delete_book(name, author):
    for book in books:
        if book['name'] == name and book['author'] == author:
            books.remove(book)
            return True
    return False


def read_book(name, author):
    for book in books:
        if book['name'] == name and book['author'] == author:
            book['read'] = True
            return True
    return False



