from django.core.management.base import BaseCommand

import telebot
from shop.models import Product

bot = telebot.TeleBot("6784413566:AAHc19yxI45oaeqcjJNQv43Dlm6nonN6sww") # Вставьте сюда свой токен


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")


@bot.message_handler(commands=['products'])
def products(message):
    products = Product.objects.all()
    for product in products:
        response = f"Название: {product.name}\nЦена: {product.price}"
        bot.send_message(message.chat.id, response)


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


@bot.message_handler(commands=['help'])
def help_command(message):
    response = "Доступные команды:\n"
    response += "/start - Запуск бота\n"
    response += "/products - Просмотреть список товаров\n"
    response += "/help - Показать доступные команды\n"
    response += "/add <product_name> <product_price> - Добавить товар в базу данных"
    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['add'])
def add_product(message):
    command_parts = message.text.split(' ')
    if len(command_parts) != 3:
        bot.send_message(message.chat.id, "Неверный формат команды. Используйте /add <product_name> <product_price>")
        return
    product_name = command_parts[1]
    product_price = command_parts[2]
    Product.objects.create(name=product_name, price=product_price)
    bot.send_message(message.chat.id, f"Товар '{product_name}' Цена товара '{product_price}' добавлено в базу данных")


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")
