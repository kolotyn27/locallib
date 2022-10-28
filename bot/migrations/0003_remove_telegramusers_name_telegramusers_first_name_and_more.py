# Generated by Django 4.1.1 on 2022-10-27 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bot", "0002_alter_telegramusers_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="telegramusers",
            name="name",
        ),
        migrations.AddField(
            model_name="telegramusers",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Имя пользователя"
            ),
        ),
        migrations.AddField(
            model_name="telegramusers",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Имя пользователя"
            ),
        ),
    ]
