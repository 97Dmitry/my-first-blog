import telebot
import re
import prod_settings

bot = telebot.TeleBot(prod_settings.TGBOT_TOKEN)

bot_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
bot_keyboard.row('Информация о сайте', 'Связь с администрацией')

HAY = re.compile(r'^(.*?)(how are you|как дела)(.*?)$')  # Регулярка для ответа


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, Вы запустили бота сайта PostBlog, что бы запустить меню: введите /menu')


@bot.message_handler(commands=['menu'])
def show_menu(message):
    bot.send_message(message.chat.id, 'Меню', reply_markup=bot_keyboard)


@bot.message_handler(commands=['commands'])
def show_command(message):
    bot.send_message(message.chat.id, '/start\n/menu')


@bot.message_handler(content_types=['text'])
def answer_on_message(message):
    if HAY.search(message.text.lower()):
        bot.send_message(message.chat.id, 'Great')
    elif message.text == 'Информация о сайте':
        bot.send_message(message.chat.id, 'Сайт BlogPost создан с применением Python и фреймворка Django. '
                                          'Так же в создании используются множества других языков и фреймворков. '
                                          ' Что бы ознакомится с исходным кодом, перейдите на GitHub проекта '
                                          '- https://github.com/97Dmitry')
    elif message.text == 'Связь с администрацией':
        bot.send_message(message.chat.id, 'Для связи используйте https://t.me/PM_White')

    else:
        bot.send_message(message.chat.id, 'Таких слов я не понимаю(')
        bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAECFAABYFSW6VKZFVl2VOCgZmk_v7MK3AcAAngBAAIeQaUI9QcDyQvOvfMeBA')
        bot.send_message(message.chat.id, 'Вы можете узнать список доступных команд, написав /commands')


bot.polling()
