from django.shortcuts import render
from django.db.models import Q
from .models import Book
from django.contrib.auth.decorators import login_required


def index(request):
    """Домашняя страница"""
    return render(request, "catalog/index.html")


def books(request, page):
    """выводит список книг"""
    # books_on_page можно вынети в настройки
    books_on_page = 4
    books_count = Book.objects.count()
    # books = Book.objects.order_by("id")
    books = []
    for book_id in range((page - 1) * books_on_page + 1, page * books_on_page + 1):
        if book_id <= books_count:
            books.append(Book.objects.get(id=book_id))

    prev_page = page - 1
    next_page = page + 1
    context = {
        "books": books,
        "next_page": next_page,
        "page": page,
        "prev_page": prev_page,
    }
    return render(request, "catalog/books.html", context)


def book(request, book_id):
    """Выводит информацию о книге"""
    book = Book.objects.get(id=book_id)
    context = {
        "name": book.name.capitalize(),
        "author": book.author,
        "genres": book.genres,
        "descript": book.descript.capitalize(),
        "file": book.file,
        "cover": book.cover,
    }
    return render(request, "catalog/book.html", context)


def audio_books(request):
    """Страница с аудиокнигами"""
    return render(request, "catalog/audio_books.html")


def search_result(request):
    """страница результатов поиска"""
    query = request.GET.get("q").lower()
    query_list = query.split(" ")
    print(query)
    context = {}
    if len(query_list) > 1:
        books_list = Book.objects.filter(
            Q(name__contains=query)
            | Q(author__first_name__contains=query_list[0])
            & Q(author__last_name__contains=query_list[1])
        )
        books_list = Book.objects.filter(
            Q(name__contains=query)
            | Q(author__first_name__contains=query_list[1])
            & Q(author__last_name__contains=query_list[0])
        )
    else:
        books_list = Book.objects.filter(
            Q(name__contains=query)
            | Q(author__first_name__contains=query)
            | Q(author__last_name__contains=query)
        )
    if books_list:
        context["books_list"] = books_list
    # books_list = Book.objects.filter(author__icontains=query)
    context = {
        "books_list": books_list,
    }
    return render(request, "catalog/search_result.html", context)
