import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot("8601263001:AAGud6KjlZ4HkgSq1U1E7l7n4VrBYYPWh9s")

# Menu buttons
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("tamil animation collection"),
        KeyboardButton("tamil movies collection"),
        KeyboardButton("editing scence pack"),
        KeyboardButton("vfx"),
        KeyboardButton("tamil dub movie collection")
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Select collection 👇", reply_markup=main_menu())

@bot.message_handler(func=lambda message: True)
def reply(message):
    text = message.text.lower()

    # Animation collection
    if text == "tamil animation collection":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            KeyboardButton("Doraemon"),
            KeyboardButton("Death note"),
            KeyboardButton("Solo leveling"),
            KeyboardButton("Naruto classic"),
            KeyboardButton("Naruto shippuden"),
            KeyboardButton("Demon slayer"),
            KeyboardButton("Attack on titain"),
            KeyboardButton("Shinchan")
        )
        bot.send_message(message.chat.id, "Choose animation 👇", reply_markup=markup)

    elif text == "doraemon":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MESSAGE_ID1)
    elif text == "solo leveling":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MESSAGE_ID1)
    elif text == "naruto classic":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MESSAGE_ID1)
    elif text == "naruto shippuden":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MESSAGE_ID1)
    elif text == "death note":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MESSAGE_ID1)
    elif text == "demon slayer":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MESSAGE_ID1)
    elif text == "attack on titain":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MESSAGE_ID1)
    elif text == "shinchan":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MESSAGE_ID2)

    # Movies collection
    elif text == "tamil movies collection":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            KeyboardButton("Leo"),
            KeyboardButton("Jailer")
        )
        bot.send_message(message.chat.id, "Choose movie 👇", reply_markup=markup)

    elif text == "leo":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MESSAGE_ID3)

    elif text == "jailer":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MESSAGE_ID4)

    # Dub movies
    elif text == "tamil dub movie collection":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            KeyboardButton("Avengers"),
            KeyboardButton("Spiderman")
        )
        bot.send_message(message.chat.id, "Choose dub movie 👇", reply_markup=markup)

    elif text == "avengers":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MESSAGE_ID5)

    elif text == "spiderman":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MESSAGE_ID6)

    else:
        bot.send_message(message.chat.id, "Type /start bro")

bot.polling()
