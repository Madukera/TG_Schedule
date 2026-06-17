import telebot
from telebot import types
import json
from datetime import datetime, timedelta

# Import and store your API-token from token.txt file
with open("token.txt", "r") as file:
    storeToken = file.read().strip()

bot = telebot.TeleBot(storeToken)

# Welcome message for /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hi, you just launched the cleaning bot! type \"/cleaning\"")

@bot.message_handler(commands=['cleaning'])
def check_schedule(message):
    load = load_data_json()
    current = get_current_saturday()
    next_saturday = get_next_saturday()

    for entry in load["schedule"]:
        if entry["week_start"] == current:
            bot.send_message(message.from_user.id, f" On this week cleaning: {entry["name"]}")
        if entry["week_start"] == next_saturday:
            bot.send_message(message.from_user.id, f" On next week cleaning: {entry["name"]}")

@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("cleaning")
    markup.add(item1)
    bot.send_message(message.chat.id, "Choose your schedule", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def echo_message(message):
    user_id = message.from_user.id
    message_text = message.text
    if message_text.lower() == "cleaning":
        # bot.send_message(user_id, message.text)
        # bot.reply_to(message, str(user_id))
        check_schedule(message)
        print(f"Someone request user_id: {user_id}")
        print(f"request user_id: {user_id}")
    else:
        # bot.send_message(user_id, message.text)
        print(f"Non request user_id: {user_id}")


def load_data_json():
    with open("users.json", "r") as date:
        data = json.load(date)
        return data

def get_current_saturday():
    today = datetime.today()
    saturday_convert = today - timedelta(days = today.weekday() - 5)
    saturday = saturday_convert.strftime("%Y-%m-%d")
    return saturday

def get_next_saturday():
    current = get_current_saturday()
    next_saturday_date = datetime.strptime(current, "%Y-%m-%d")
    next_saturday = next_saturday_date + timedelta(days = 7)
    return next_saturday.strftime("%Y-%m-%d")

bot.infinity_polling(none_stop=True)