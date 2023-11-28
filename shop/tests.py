import unittest
from unittest.mock import MagicMock
from .management.commands.run_telegram_bot import start, food, help_command, add_food


class TestBot(unittest.TestCase):

    def test_start(self):
        message = MagicMock()
        message.chat.id = 623917543
        start(message)

    def test_help_command(self):
        message = MagicMock()
        message.chat.id = 623917543
        help_command(message)

    def test_food(self):
        message = MagicMock()
        message.chat.id = 623917543
        food(message)

    def test_add_food_command(self):
        message = MagicMock()
        message.chat.id = 623917543
        add_food(message)


if __name__ == '__main__':
    unittest.main()