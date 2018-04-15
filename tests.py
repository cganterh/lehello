"""Tests for lehello module."""


from unittest import (
    main,
    TestCase,
)

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


class TestLeHelloModule(TestCase):
    """Test lehello module contents."""

    def test_lehello_has_no_public_attributes(self):
        """Test that lehello has no public attributes."""
        self.assertEqual([], [a for a in dir(lehello) if is_public(a)])


if __name__ == '__main__':
    main()
