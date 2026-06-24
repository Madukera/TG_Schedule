import apscheduler.schedulers.background
import telebot
import json
from apscheduler.schedulers.background import BackgroundScheduler
from telebot import types
from datetime import datetime, timedelta

# Import and store your API-token from token.txt file
with open("token.txt", "r") as file:
    storeToken = file.read().strip()

bot = telebot.TeleBot(storeToken)

# Welcome message for /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hi, you just launched the cleaning bot! type \"/cleaning\"")

# Bot message with button
@bot.message_handler(commands=['cleaning'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("who is cleaning?")
    markup.add(item1)
    bot.send_message(message.chat.id, "Choose your schedule", reply_markup=markup)

def check_schedule(message):
    found_current = False
    found_next_saturday = False
    load = load_data_json()
    current = get_current_saturday()
    next_saturday = get_next_saturday()

    for entry in load["schedule"]:
        if entry["week_start"] == current:
            bot.send_message(message.from_user.id, f" On this week cleaning: {entry["name"]}")
            found_current = True
        if entry["week_start"] == next_saturday:
            bot.send_message(message.from_user.id, f" On next week cleaning: {entry["name"]}")
            found_next_saturday = True
    if not found_current:
        print("in current there is no dates or there are empty")
    if not found_next_saturday:
        print("in next_saturday there is no dates or there are empty")




@bot.message_handler(content_types=['text'])
def echo_message(message):
    user_id = message.from_user.id
    message_text = message.text
    if message_text.lower() == "who is cleaning?":
        check_schedule(message)
        print(f"Someone request user_id: {user_id}")
    else:
        print(f"Non request user_id: {user_id}")

def load_data_json():
    with open("users.json", "r") as date:
        data = json.load(date)
        return data

def get_user_id(name):
    load = load_data_json()
    for user in load["users"]:
        if user["name"] == name:
            return user["user_id"]
    return None

def reminder():
    load = load_data_json()
    current = get_current_saturday()
    for entry in load["schedule"]:
        if entry["week_start"] == current:
                user_id = get_user_id(entry["name"])
                if user_id is not None:
                    bot.send_message(user_id, f"{entry["name"]}, you are cleaning on this week, don't forget:)")
                else:
                    print(f"None for: user_id \"{entry["name"]}\"")

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

def RadScheduler():
    phon = BackgroundScheduler()
    phon.add_job(reminder, trigger = 'cron', day_of_week=5, hour=9)
    phon.start()



RadScheduler()
bot.infinity_polling(none_stop=True)