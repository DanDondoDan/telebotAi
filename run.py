import logging

logger = logging.getLogger(__name__)

from telebot_ai.bot_AI import up

from token import TOKEN, PORT

if __name__=="__main__":
    updater.start_webhook(listen='0.0.0.0',
						  port=PORT,
						  url_path=TOKEN)
    up.bot.setWebhook('https://dashboard.heroku.com/apps/telebotai'+TOKEN)
    up.start_polling(clean=True)
	up.idle()
