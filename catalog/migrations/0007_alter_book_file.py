# Generated by Django 4.1.1 on 2022-10-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_book_cover"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="file",
            field=models.FileField(
                blank=True, null=True, upload_to="files", verbose_name="Файл"
            ),
        ),
    ]