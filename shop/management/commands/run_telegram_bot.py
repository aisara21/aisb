from django.core.management.base import BaseCommand

import telebot
from shop.models import Food

bot = telebot.TeleBot("6784413566:AAHc19yxI45oaeqcjJNQv43Dlm6nonN6sww")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")


@bot.message_handler(commands=['foods'])
def food(message):
    foods = Food.objects.all()
    for food in foods:
        response = f"Название: {food.name}\nЦена: {food.price}"
        bot.send_message(message.chat.id, response)


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


@bot.message_handler(commands=['help'])
def help_command(message):
    response = "Доступные команды:\n"
    response += "/start - Запуск бота\n"
    response += "/foods - Просмотреть меню\n"
    response += "/help - Показать доступные команды\n"
    response += "/add <food_name> <food_price> - Добавить еду в базу данных"
    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['add'])
def add_food(message):
    command_parts = message.text.split(' ')
    if len(command_parts) != 3:
        bot.send_message(message.chat.id, "Неверный формат команды. Используйте /add <food_name> <food_price>")
        return
    food_name = command_parts[1]
    food_price = command_parts[2]
    Food.objects.create(name=food_name, price=food_price)
    bot.send_message(message.chat.id, f"Еда '{food_name}' Цена еды '{food_price}' добавлено в базу данных")


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")
