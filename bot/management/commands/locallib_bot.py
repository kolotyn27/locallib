from unicodedata import name
from django.core.management.base import BaseCommand
from bot.models import TelegramUsers
from catalog.views import search

from telegram.utils.request import Request
from telegram import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    Bot,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler

# функция обработки команды '/start'
def start(update, context):
    update.message.reply_text("Введите название или али автора")


# функция обработки команды '/help'
def help(update, context):
    text = "Для поиска нужной вам книги напишите ее название или автора"
    update.message.reply_text(text)


# функция обработки не распознных команд
def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Извините, я не знаю такой команды",
    )


# функция обработки текстовых сообщений
def echo(update, context):
    chat_id = update.message.chat.id
    # проверка наличия ID среди пользователей
    # сделать декоратором и обернуть в него все запросы
    TelegramUsers.objects.get_or_create(
        external_id=chat_id,
        defaults={
            "first_name": update.message.chat.first_name,
            "last_name": update.message.chat.last_name,
        },
    )
    query = update.message.text.lower()
    books_list = search(query)
    if books_list:
        for book in books_list:
            update.message.reply_document(
                filename=book.name + ".epub",
                document=book.file,
            )
    else:
        update.message.reply_text("По вашему запросу ничего не найдено")
    # другой вариант отправки сообщения
    # context.bot.send_message(chat_id=update.effective_chat.id, text=text)


class Command(BaseCommand):
    """Команда для запуска бота через manage.py"""

    def handle(self, *args, **kwargs):

        # можно вынести TOKEN в файл с настройками
        TOKEN = "5667460915:AAH9Byb0tkOdx0bQSm_Gzs2dEwa78ilTqbM"

        updater = Updater(token=TOKEN)
        dispatcher = updater.dispatcher

        request = Request(
            connect_timeout=0.5,
            read_timeout=1,
        )
        bot = Bot(
            request=request,
            token=TOKEN,
        )
        print(bot.get_me())

        # обработчик команды '/start'
        start_handler = CommandHandler("start", start)
        dispatcher.add_handler(start_handler)

        # обработчик команды '/help'
        help_handler = CommandHandler("help", help)
        dispatcher.add_handler(help_handler)

        # обработчик текстовых сообщений
        echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
        dispatcher.add_handler(echo_handler)

        # обработчик не распознанных команд
        unknown_handler = MessageHandler(Filters.command, unknown)
        dispatcher.add_handler(unknown_handler)

        # запуск прослушивания сообщений
        updater.start_polling()
        # обработчик нажатия Ctrl+C
        updater.idle()
