import telebot

# Import and store your API-token from toke.txt file
Token = open("token.txt", "r")
storeToken = Token.read()
bot = telebot.TeleBot(storeToken)


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    if message.txt == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем могу помочь?")
    elif message.txt == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю")

bot.polling(none_stop=True, interval=0)
