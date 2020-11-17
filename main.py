import os
from dotenv import load_dotenv
# import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import message
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
load_dotenv()

TG_TOKEN = os.getenv('TELEGRAM_TOKEN')
updater = Updater(token=TG_TOKEN)
# CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
dispatcher = updater.dispatcher
COMMAND_LIST = ('/start', 'help', )


# bot = telegram.Bot(token=TG_TOKEN)
#
#
# def textMessage(bot, update):
#     response = 'Получил Ваше сообщение: ' + update.message.text
#     bot.send_message(chat_id=update.message.chat_id, text=response)
#
#
# # def send_message(message):
# #     bot = telegram.Bot(token=TG_TOKEN)
# #     return bot.send_message(chat_id=CHAT_ID, text=message)
# def print_test(bot, update):
#     print(bot)
#     print(update.message.chat_id)
#
# def startCommand(bot, update):
#     print_test(bot, update)
#     bot.send_message(chat_id=update.message.chat_id, text='Доброе утро, давай пообщаемся?')
#
# start_command_handler = CommandHandler('start', startCommand)
# text_message_handler = MessageHandler(Filters.text, textMessage)
# dispatcher.add_handler(start_command_handler)
# dispatcher.add_handler(text_message_handler)
# updater.start_polling(clean=True)
# updater.idle()
#
#
# #def main():
# #   # send_message("Доброе утро!")
# #    updater.start_polling(clean=True)
# #    updater.idle()
#
# #if __name__ == '__main__':
# #    main()

# Обработка команд
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=message.START_MESSAGE)

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=message.HELP_MESSAGE)

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def echo_file(update, context):
    print(update.message)
    print(update.effective_chat)
    file_name =  update.message.document.file_name
    path = 'temp/{}'.format(file_name)
    print(path)
    file_info = context.bot.getFile(file_id = update.message.document.file_id)
    print(file_info)
    download_file = file_info.download(path)
    #with open(path, 'wb') as new_file:
    #    new_file.write(download_file)

   # context.bot.getFile(file_id = update.message.document.file_id).download(out ='temp')
 #   telegram.File

def file_load(update, context):
    print('ghbdtn')
    print(update.message)
    #print()
    #file = update.getFile(context.message.f)
# Хендлеры
#start_command_handler = CommandHandler('start', startCommand)
start_handler = CommandHandler('start', start)
help_hanlder = CommandHandler('help', help)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
file_handler = CommandHandler('loadbase', file_load)
echo_file_handler = MessageHandler(Filters.document, echo_file)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_hanlder)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(file_handler)
dispatcher.add_handler(echo_file_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()