from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import message

__list_team = []
class Team:
    def __init__(self, name, capitan, chat):
        self.__team_name = name,
        self.__team_capitan = capitan,
        self.__team_chat = chat


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

def registering_teams(update, context):
    print('sss')
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите имя команды")


def file_load(update, context):
    print('ghbdtn')
    print(update.message)
    #print()
    #file = update.getFile(context.message.f)
# Хендлеры
#start_command_handler = CommandHandler('start', startCommand)
def initial_comand_handler(dispatcher):
    start_handler = CommandHandler('start', start)
    help_hanlder = CommandHandler('help', help)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    file_handler = CommandHandler('loadbase', file_load)
    registering_teams_handler = CommandHandler('registeringteams', registering_teams)
    echo_file_handler = MessageHandler(Filters.document, echo_file)
    # Добавляем хендлеры в диспетчер
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_hanlder)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(file_handler)
    dispatcher.add_handler(echo_file_handler)
    dispatcher.add_handler(registering_teams_handler)
    return dispatcher
