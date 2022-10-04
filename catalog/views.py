from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required


def index(request):
    """Домашняя страница"""
    return render(request, "catalog/index.html")


def books(request):
    """выводит список книг"""
    books = Book.objects.order_by("name")
    context = {"books": books}
    return render(request, "catalog/books.html", context)


def book(request, book_id):
    """Выводит информацию о книге"""
    book = Book.objects.get(id=book_id)
    # name = book.name
    # author = book.author
    # genre = book.genres
    # descript = book.descript
    # file = book.file
    context = {
        "name": book.name,
        "author": book.author,
        "genres": book.genres,
        "descript": book.descript,
        "file": book.file,
    }
    return render(request, "catalog/book.html", context)
