
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai
import json
from token import ApiAI, TOKEN
import logging

logger = logging.getLogger(__name__)


def info(bot, update):
    update.message.reply_text(f'Hello I am artificial intelligent bot, i have a consciousness')


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello, lets talk?')


def textMSG(bot, update):
    request = apiai.ApiAI(ApiAI).text_request()
    request.lang = 'en'
    request.session_id = 'BatlabAIBot'
    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='I dont undersend you, repeat please!')


if __name__=="__main__":

    up = Updater(token=TOKEN)
    dispatcher = up.dispatcher
    up.dispatcher.add_handler(CommandHandler("start", start))
    up.dispatcher.add_handler(CommandHandler("textMSG", textMSG))
    up.dispatcher.add_handler(CommandHandler("info", info))

    up.start_polling(clean=True)
    up.idle()
