from django.db import models


class Author(models.Model):
    first_name = models.CharField(
        max_length=200,
        help_text="Введите имя автора",
        verbose_name="Имя",
    )
    last_name = models.CharField(
        max_length=200,
        help_text="Введите фамилию автора",
        verbose_name="Фамилия",
    )

    def __str__(self):
        return "%s %s" % (self.first_name.capitalize(), self.last_name.capitalize())


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Введите наименование жанра",
        verbose_name="Жанр",
    )

    def __str__(self):
        return self.name.capitalize()


class Book(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Введите название книги",
        verbose_name="Название",
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Автор",
    )
    genres = models.ManyToManyField(
        Genre,
        verbose_name="Жанр",
    )
    descript = models.TextField(
        help_text="Введите описаниние книги",
        verbose_name="Описание",
    )
    file = models.FileField(
        verbose_name="Файл",
        null=True,
        blank=True,
    )
    # cover = models.ImageField()

    def __str__(self):
        return self.name
