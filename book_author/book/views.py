from django.shortcuts import render
from .models import Book, Author


def home(request):
    author = Author.objects.all()
    book = Book.objects.all()
    return render(request, "book_author.html", {"authors": author, "books": book})
