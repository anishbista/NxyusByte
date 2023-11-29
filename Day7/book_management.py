class Book:
    def __init__(self, isbn, title, author, quantity):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.quantity = quantity

    def display(self):
        return f"ISBN: {self.isbn} Title: {self.title} Author: {self.author} Quantity: {self.quantity} "


books = {}


def add_books(isbn, title, author, quantity):
    if isbn not in books:
        book = Book(isbn, title, author, quantity)
        books[isbn] = book
    else:
        raise ValueError("Book already exists.")
    print(books)


def update_books(isbn, title, author, quantity):
    if isbn in books:
        books[isbn].title = title
        books[isbn].author = author
        books[isbn].quantity = quantity
    else:
        raise ValueError("Book not found")


def remove_books(isbn):
    if isbn in books:
        del books[isbn]
    else:
        raise ValueError("Book not found")
