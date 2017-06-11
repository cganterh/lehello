from telegram.ext import CommandHandler


def hello(bot, update):
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text="Hi all, I'm {bot.first_name}.".format(bot=bot)
    )


handler = CommandHandler('hi', hello)
