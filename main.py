import os
from dotenv import load_dotenv
# import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import message
from comands import *
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
load_dotenv()

TG_TOKEN = os.getenv('TELEGRAM_TOKEN')
updater = Updater(token=TG_TOKEN)
# CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
dispatcher = updater.dispatcher
COMMAND_LIST = ('/start', 'help', )
print('Start')

def main():
    dispatcher = updater.dispatcher
    dispatcher = initial_comand_handler(dispatcher)
    # Начинаем поиск обновлений
    updater.start_polling(clean=True)
    # Останавливаем бота, если были нажаты Ctrl + C
    updater.idle()

if __name__ == '__main__':
    main()

