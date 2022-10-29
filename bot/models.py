from django.db import models


class TelegramUsers(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name="ID пользователя",
        unique=True,
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name="Имя пользователя",
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="Фамилия пользователя",
        null=True,
        blank=True,
    )

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = "Телеграм пользователь"
        verbose_name_plural = "Телеграм пользователи"
