"""Определяем схему URL для приложения catalog"""

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "catalog"

urlpatterns = [
    # Домашняя страница
    path("", views.index, name="index"),
    # path("books", views.books, name="books"),
    path("books/<int:page>", views.books, name="books"),
    path("book/<int:book_id>", views.book, name="book"),
    path("audio_books", views.audio_books, name="audio_books"),
    path("search_result", views.search_result, name="search_result"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
