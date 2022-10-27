from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Телеграмм-бот"

    def handler(self):
        pass
