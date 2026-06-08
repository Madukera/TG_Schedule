import telebot
import json
from datetime import datetime, timedelta
import time

# Import and store your API-token from toke.txt file
with open("token.txt", "r") as file:
    storeToken = file.read()
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
# Welcome message for /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi, you just launched the cleaning bot!")

@bot.message_handler(content_types=['text'])
def echo_message(message):
    user_id = message.from_user.id
    message_text = message.text
    if message_text.lower() == "hello":
        bot.reply_to(message, str(user_id))
    else:
        bot.send_message(user_id, message.text)

def load_data_json():
    with open("users.json", "r") as date:
        data = json.load(date)
        return data


def get_current_monday():
    today = datetime.today()
    monday_convert = today - timedelta(days = today.weekday())
    monday = monday_convert.strftime("%Y-%m-%d")
    return monday

def get_next_monday():
    current = get_current_monday()
    next_monday_date = datetime.strptime(current, "%Y-%m-%d")
    next_monday = next_monday_date + timedelta(days = 7)
    return next_monday.strftime("%Y-%m-%d")

def check_schedule():
    with open("users.json", "r") as date:
        date = json.load(date)



x = get_current_monday()
y = get_next_monday()
print(y)



bot.infinity_polling()
