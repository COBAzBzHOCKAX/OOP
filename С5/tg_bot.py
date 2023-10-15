import telebot

TOKEN = "6497091642:AAEvpL4Rv-6WTu42z_BuV4QAEJes4sDaPt8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}')

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "Хороший мем XDD")

bot.polling(none_stop=True)