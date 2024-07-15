import telegram
import random
from webserver import keep_alive
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

my_secret = ''

bot = telegram.Bot(token=my_secret)

commands = [
    telegram.BotCommand('alien', 'Инопланетяяяянее...'),
    # telegram.BotCommand('lishniy', 'Вы тут лишний...')
]

bot.set_my_commands(commands)

user_last_call_time = {}


def alien(update, context):
    user_id = update.effective_user.id
    username = update.effective_user.username

    last_call_time = user_last_call_time.get(user_id)

    if last_call_time and time.time() - last_call_time < 60:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=
            "В следующий раз ты сможешь стать инопланетянином только через минуту((("
        )

    else:
        # percent = 100 if user_id == 257486435 else random.randint(0, 100)
        percent = random.randint(0, 100)
        message = f'@{username}, вы стали инопланетянином на {percent}% 👽👽👽'

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=message)

        if percent == 100:
            #context.bot.send_message(chat_id=update.effective_chat.id, text="🎉")
            sticker_id = "CAACAgIAAxkBAAEBBLhk_28ZMPi-hwrYEMnQgf7qTTSt3gACKDUAAqxGAUiLSmCPsJGECTAE"
            chat_id = update.effective_chat.id
            context.bot.send_sticker(chat_id=chat_id, sticker=sticker_id)

        if percent == 0:
            sticker_id = "CAACAgIAAxkBAAEBBLBk_22HcohudOWUqbYbYAQ6AAE6qHYAAjxAAAL51QFIcGFwmGWhdH8wBA"
            chat_id = update.effective_chat.id
            context.bot.send_sticker(chat_id=chat_id, sticker=sticker_id)

        user_last_call_time[user_id] = time.time()


def lishniy(update, context):
    user_id = update.effective_user.id
    username = update.effective_user.username

    percent = 100 if user_id == 257486435 else random.randint(0, 0)
    # percent = random.randint(0, 100)
    message = f'@{username}, вы тут лишний на {percent}%'

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

    if percent == 100:
        # sticker_id = "CAACAgIAAxkBAAECP15lanWvg0UXcXDU6V-k0SBVow7WnQACAjYAAmHQKEuMEocP-OpuJzME"
        chat_id = update.effective_chat.id
        # context.bot.send_sticker(chat_id=chat_id, sticker=sticker_id)
        context.bot.send_photo(
            chat_id=chat_id,
            # photo=
            # 'https://sun9-78.userapi.com/impf/c845419/v845419336/d496d/FPZmU-cQI2I.jpg?size=720x717&quality=96&sign=ce2378b62780df4cce81ae3595490b4d&type=album'
            photo='https://st2.depositphotos.com/1594920/12419/i/450/depositphotos_124195480-stock-photo-european-shorthair-kitten-1-month.jpg')


updater = Updater(my_secret, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('alien', alien))
dispatcher.add_handler(
  MessageHandler(
    Filters.text & (~Filters.command) & Filters.regex(fr'(?i)^{bot.username}'), alien))
dispatcher.add_handler(CommandHandler('lishniy', lishniy))

keep_alive()
updater.start_polling()
updater.idle()
