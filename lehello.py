"""Provide a simple greeting handler for a Le bot."""


from telegram.ext import CommandHandler as _CommandHandler


def _hello(bot, update):
    """Greet the user using own name."""
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text="Hi all, I'm {bot.first_name}.".format(bot=bot)
    )


_handler = _CommandHandler('hi', _hello)
