import telebot

# Import and store your API-token from toke.txt file
Token = open("token.txt", "r")
storeToken = Token.read()
bot = telebot.TeleBot(storeToken)

'''
@bot.message_handler(content_types=['help', 'start'])
def send_welcome(message):
    if message.txt == "Hello":
        bot.send_message(message.from_user.id, "Hi, how can I help you?")
    elif message.txt == "/help":
        bot.send_message(message.from_user.id, "Write \'Hello\'")
    else:
        bot.send_message(message.from_user.id, "I don't understand you")
'''

@bot.message_handler(content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)
    bot.send_message(message.from_user.id, "Hello")
    print(message.from_user.id)

bot.infinity_polling()
