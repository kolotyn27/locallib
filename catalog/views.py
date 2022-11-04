from django.shortcuts import render
from django.db.models import Q
from .models import Book
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET


@require_GET
def index(request):
    """Домашняя страница"""
    return render(request, "catalog/index.html")


@require_GET
def books(request, page):
    """выводит список книг"""
    # books_on_page можно вынети в настройки
    books_on_page = 4
    books_count = Book.objects.count()
    books = []
    prev_page = page - 1
    next_page = page + 1
    for book_id in range((page - 1) * books_on_page + 1, page * books_on_page + 1):
        if book_id <= books_count:
            books.append(Book.objects.get(id=book_id))
        if book_id + 1 > books_count:
            next_page = 0

    context = {
        "books": books,
        "next_page": next_page,
        "page": page,
        "prev_page": prev_page,
    }
    return render(request, "catalog/books.html", context)


@require_GET
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


@require_GET
def audio_books(request):
    """Страница с аудиокнигами"""
    return render(request, "catalog/audio_books.html")


def search(query):
    """Поиск книги по названию и автору"""
    query_list = query.split(" ")
    if len(query_list) > 1:
        books_list = Book.objects.filter(
            Q(name__contains=query)
            | Q(author__first_name__contains=query_list[1])
            & Q(author__last_name__contains=query_list[0])
            | Q(author__first_name__contains=query_list[0])
            & Q(author__last_name__contains=query_list[1])
        )
    else:
        books_list = Book.objects.filter(
            Q(name__contains=query)
            | Q(author__first_name__contains=query)
            | Q(author__last_name__contains=query)
        )
    return books_list


@require_GET
def search_result(request):
    """страница результатов поиска"""
    context = {}
    query = request.GET.get("q").lower()
    books_list = search(query)
    if books_list:
        context["books_list"] = books_list
    context = {
        "books_list": books_list,
    }
    return render(request, "catalog/search_result.html", context)
