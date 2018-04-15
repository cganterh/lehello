"""Tests for lehello module."""


from unittest import (
    main,
    TestCase,
)

from unittest.mock import MagicMock

from pkg_resources import load_entry_point
from telegram.ext import CommandHandler

import lehello


def is_private(string):
    """Return ``True`` if string is a private attribute name."""
    return string.startswith('_')


def is_public(string):
    """Return ``True`` if string is a public attribute name."""
    return not is_private(string)


class LeHelloHandlerTestCase(TestCase):
    """Test case with a loaded lehello handler."""

    def setUp(self):
        """Load the lehello handler."""
        self.handler = load_entry_point(
            'lehello', 'le.handlers', 'le_hello_handler')


class TestLeHelloHandler(LeHelloHandlerTestCase):
    """Test a lehello handler."""

    def test_handlers_type(self):
        """Test that the handler is an instance of CommandHandler."""
        self.assertIsInstance(
            self.handler,
            CommandHandler,
            'lehello.handler is not an instance of CommandHandler.'
        )


class TestLeHelloHandlerCallback(LeHelloHandlerTestCase):
    """Test the behavior of the callback function.

    This callback should send a message saying hi and including the
    name of the bot.
    """

    def setUp(self):
        """Set up a call to the callback."""
        super().setUp()
        self.bot = MagicMock()
        self.update = MagicMock()
        self.bot.first_name = 'cris'
        self.handler.callback(self.bot, self.update)

    def test_send_message_is_called(self):
        """Test that bot.send_message() was called."""
        self.bot.send_message.assert_called_with(
            self.update.message.chat_id,
            "Hi all, I'm {name}.".format(name='cris')
        )


class TestLeHelloModule(TestCase):
    """Test lehello module contents."""

    def test_lehello_has_no_public_attributes(self):
        """Test that lehello has no public attributes."""
        self.assertEqual([], [a for a in dir(lehello) if is_public(a)])


if __name__ == '__main__':
    main()
