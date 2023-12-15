from django.shortcuts import render
from .models import Author, Book, Category


def home(request):
    books = Book.objects.select_related("author").prefetch_related("category").all()

    for book in books:
        print(book)
        print(book.author)
        for category in book.category.all():
            print(category)
    return render(request, "book_author.html", {"books": book})
