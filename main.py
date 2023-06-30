import telegram
import random
import os
from webserver import keep_alive
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telebot as tg
import threading

my_secret = os.environ['bot_token']

bot = telegram.Bot(token=my_secret)

# bot = tg.TeleBot(token=my_secret)

commands = [telegram.BotCommand('start', 'Инопланетяяяянее...')]

bot.set_my_commands(commands)

user_last_call_time = {}

def start(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Hello!")

def mention(update, context):
  user_id = update.effective_user.id

  last_call_time = user_last_call_time.get(user_id)

  if last_call_time and time.time() - last_call_time < 60:
    context.bot.send_message(
      chat_id=update.effective_chat.id,
      text=
      "В следующий раз ты сможешь стать инопланетянином только через минуту(((")

  else:

    percent = random.randint(0, 100)

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f'Вы стали инопланетянином на {percent}% 👽👽👽')

    user_last_call_time[user_id] = time.time()

updater = Updater(my_secret, use_context=True)
my_secret = os.environ['bot_token']
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', mention))

dispatcher.add_handler(
  MessageHandler(
    Filters.text & (~Filters.command) & Filters.regex(f'^(?i){bot.name}'),
    mention))

keep_alive()
updater.start_polling()
updater.idle()