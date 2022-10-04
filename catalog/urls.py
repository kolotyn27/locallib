"""Определяем схему URL для приложения catalog"""

from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    # Домашняя страница
    path("", views.index, name="index"),
    path("books", views.books, name="books"),
    path("book/<int:book_id>", views.book, name="book"),
]
