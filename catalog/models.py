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

    def save(self):
        self.first_name = self.first_name.lower()
        self.last_name = self.last_name.lower()
        return super(Author, self).save()

    def __str__(self):
        return "%s %s" % (self.first_name.capitalize(), self.last_name.capitalize())

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Введите наименование жанра",
        verbose_name="Жанр",
    )

    def save(self):
        self.name = self.name.lower()
        return super(Genre, self).save()

    def __str__(self):
        return self.name.capitalize()

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


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
        upload_to="files",
        verbose_name="Файл",
        null=True,
        blank=True,
    )
    cover = models.ImageField(
        upload_to="images",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name.capitalize()

    def save(self):
        self.name = self.name.lower()
        self.descript = self.descript.lower()
        return super(Book, self).save()

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
