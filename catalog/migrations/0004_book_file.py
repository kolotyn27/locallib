# Generated by Django 4.1.1 on 2022-09-29 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_remove_book_file_alter_author_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="file",
            field=models.FileField(
                blank=True, null=True, upload_to="", verbose_name="Файл"
            ),
        ),
    ]
