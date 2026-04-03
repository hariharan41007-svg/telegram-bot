import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot("8743365765:AAErc_VNcfbqegNJ3Ay2tUSHx4Bleeb4WX0")

# MAIN MENU
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("tamil animation collection"),
        KeyboardButton("tamil movies collection"),
        KeyboardButton("editing scene pack"),
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

    # ================= ANIMATION =================
    if text == "tamil animation collection":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            KeyboardButton("Doraemon"),
            KeyboardButton("Death note"),
            KeyboardButton("Solo leveling"),
            KeyboardButton("Naruto classic"),
            KeyboardButton("Naruto shippuden"),
            KeyboardButton("Demon slayer"),
            KeyboardButton("Attack on titan"),
            KeyboardButton("Shinchan")
        )
        bot.send_message(message.chat.id, "Choose animation 👇", reply_markup=markup)

    elif text == "doraemon":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MSG_DORAEMON)

    elif text == "death note":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MSG_DEATHNOTE)

    elif text == "naruto classic":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MSG_NARUTO1)

    elif text == "naruto shippuden":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MSG_NARUTO2)

    elif text == "demon slayer":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MSG_DEMON)

    elif text == "attack on titan":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MSG_AOT)

    elif text == "shinchan":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MSG_SHINCHAN)

    # SOLO LEVELING MENU
    elif text == "solo leveling":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            KeyboardButton("SOLO LEVELING EP1"),
            KeyboardButton("SOLO LEVELING EP2"),
            KeyboardButton("SOLO LEVELING EP3")
        )
        bot.send_message(message.chat.id, "Choose episode 👇", reply_markup=markup)

    elif "solo leveling ep1" in text or "so1" in text:
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MSG_SOLO1)

    elif "solo leveling ep2" in text or "so2" in text:
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MSG_SOLO2)

    elif "solo leveling ep3" in text or "so3" in text:
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MSG_SOLO3)

    # ================= MOVIES =================
    elif text == "tamil movies collection":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            KeyboardButton("Leo"),
            KeyboardButton("Jailer")
        )
        bot.send_message(message.chat.id, "Choose movie 👇", reply_markup=markup)

    elif text == "leo":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MSG_LEO)

    elif text == "jailer":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MSG_JAILER)

    # ================= DUB MOVIES =================
    elif text == "tamil dub movie collection":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            KeyboardButton("Avengers"),
            KeyboardButton("Spiderman")
        )
        bot.send_message(message.chat.id, "Choose dub movie 👇", reply_markup=markup)

    elif text == "avengers":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MSG_AVENGERS)

    elif text == "spiderman":
        bot.forward_message(message.chat.id, FROM_CHAT_ID, MSG_SPIDERMAN)

    # ================= DEFAULT =================
    else:
        bot.send_message(message.chat.id, "Type /start bro")


bot.polling()
