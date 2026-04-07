import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# 🔑 BOT TOKEN
BOT_TOKEN = "8743365765:AAErc_VNcfbqegNJ3Ay2tUSHx4Bleeb4WX0"
bot = telebot.TeleBot(BOT_TOKEN)

DATA = {

    "Naruto Season 1": [
        "EP1_FILE_ID",
        "EP2_FILE_ID",
        "EP3_FILE_ID",
        "EP4_FILE_ID",
        "EP5_FILE_ID"
    ],

    "Naruto Season 2": [
        "PASTE_ID"
    ],

    "Naruto Season 3": [
        "PASTE_ID"
    ],

    "Demon Slayer Season 1": [
        "PASTE_ID"
    ],

    "Demon Slayer Season 2": [
        "PASTE_ID"
    ],

    "Solo Leveling Season 1": [
        "BQACAgUAAxkBAAMhadUXMXhi2Ym-Z4h6_Mo8a7LIRWoAAlgfAAKdg1lWjgZEuFa32Rk7BA",
        "BQACAgUAAxkBAAMiadUXMeqolUWhzbY8WQHdyy4-VBoAAnQeAALHX2FW5FnFAaxqNIk7BA",
        "BQACAgUAAxkBAAMjadUXMaPVPp7eETatTu9EvGDsYI4AAnceAALHX2FWT2EP4DxKexw7BA",
        "BQACAgUAAxkBAAMoadUbqbVpwwTVIEZJ9R4B4yFhupsAAokgAALHX2lWkZ29eM96FJ47BA",
        "BQACAgUAAxkBAAMpadUbqThaUprDapzH--B919qawFMAAosgAALHX2lWLcBRoQwsAAFTOwQ",
        "BQACAgUAAxkBAAMqadUbqWDGCdUFOhORt2QCt1vYfNkAAowgAALHX2lWs0IvhU2Id8o7BA",
        "BQACAgUAAxkBAAMradUbqXl8FnpZ6VDT1QgXXybruZsAArEhAALHX2lWvZXf306tuzk7BA",
        "BQACAgUAAxkBAAMsadUbqRfLwNr6mV57NDYJfpu7pN4AAq4hAALHX2lWTYwQ0dtedTc7BA",
        "BQACAgUAAxkBAAMtadUbqU6Z89XuwUms7rmU12lkQEgAArAhAALHX2lWMc7WoaX8-NU7BA",
        "BQACAgUAAxkBAAMuadUbqTgunY1MwP07QEB3D5P7nLMAAq8hAALHX2lWbxK6f_Sb-eY7BA",
        "BQACAgUAAxkBAAMvadUbqRD0WEQt5ZoDw8-o_Be3cOYAAlwdAALHX3FWeCC4I-AhqPk7BA",
        "BQACAgUAAxkBAAMwadUbqV9mG-uVXyH8UPjxUUYsnQIAAl0dAALHX3FWx2B5tuNl_Ks7BA"
    ],

    "Solo Leveling Season 2": [
        "BQACAgUAAxkBAAM6adUdZzQgXqx9RGgKgUW8bdKxfYYAArgcAAIJV4FWELAwCJT8dlY7BA",
        "BQACAgUAAxkBAAM7adUdZ2kMjHPUlYvTqLcwxeRNUqIAArocAAIJV4FWJZ54ugVnrcs7BA",
        "BQACAgUAAxkBAANAadUdZ9gh3xzQ5GVPhwiac2DwFa4AAsAcAAIJV4FWuo-Y_o106qg7BA",
        "BQACAgUAAxkBAAM8adUdZ-bi9NrF_1dRxUOcVQABoLV8AAK7HAACCVeBVoVdmUBrv-zeOwQ",
        "BQACAgUAAxkBAAM9adUdZ10HiSh43l7yvZBODOub3IwAAr0cAAIJV4FW9hcKTEbGGfo7BA",
        "BQACAgUAAxkBAANCadUdZxW_OVlmmGDqMmbRh6tmk2MAAsQcAAIJV4FWJ2sILalHMCY7BA",
        "BQACAgUAAxkBAAM-adUdZyQc8gWWCm5-sQ_MDCOk0kgAAr4cAAIJV4FWIRtqPRYCwvs7BA",
        "BQACAgUAAxkBAANDadUdZ8YWi9thSg39exyqrCr8F08AAsUcAAIJV4FW-KhXYrjmelY7BA",
        "BQACAgUAAxkBAAM_adUdZyP0ozrilwvYtMQOL2WjTZwAAr8cAAIJV4FWepRTkEitUTw7BA",
        "BQACAgUAAxkBAANBadUdZ93U8qo0mK3iq_WCihzMrUwAAsIcAAIJV4FWHkpeiB2DDH47BA",
        "BQACAgUAAxkBAANGadUdZ6WuLERsn2p4FZ6qJ7s40Y4AAsgcAAIJV4FWM73tv3r6vC87BA",
        "BQACAgUAAxkBAANEadUdZwE4gBDjLEbbZnLTAhTyQrYAAsYcAAIJV4FWXPxttzP2ptU7BA",
        "BQACAgUAAxkBAANFadUdZ5JwNvqgeNLbd3KUFXlwEpUAAsccAAIJV4FW3zWMKlLleas7BA"
    ],

    "Death Note Season 1": [
        "PASTE_ID"
    ]
}

# 🎥 MOVIES
MOVIES = [
    "MOVIE_ID_1",
    "MOVIE_ID_2",
    "MOVIE_ID_3"
]

# 🔊 DUBBED MOVIES
DUB_MOVIES = [
    "DUB_ID_1",
    "DUB_ID_2"
]

# 📺 ANIME LIST + SEASONS
ANIME = {
    "Naruto": ["Season 1", "Season 2", "Season 3"],
    "Demon Slayer": ["Season 1", "Season 2"],
    "Solo Leveling": ["Season 1", "Season 2"],
    "Death Note": ["Season 1"]
}

# 🔥 MAIN MENU
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Tamil Animation Collection"),
        KeyboardButton("Tamil Movies Collection"),
        KeyboardButton("Tamil Dubbed Movies Collection"),
        KeyboardButton("Help")
    )
    return markup

# 🚀 START
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🔥 Welcome bro 😎", reply_markup=main_menu())

# 📂 FILE ID GETTER (USE THIS TO GET FILE ID)
@bot.message_handler(content_types=['video', 'document'])
def get_file_id(message):
    if message.video:
        bot.reply_to(message, message.video.file_id)
    elif message.document:
        bot.reply_to(message, message.document.file_id)

# 🧠 MAIN HANDLER
@bot.message_handler(func=lambda message: True)
def handle(message):
    text = message.text

    try:
        # 🎬 Animation Menu
        if text == "Tamil Animation Collection":
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for anime in ANIME:
                markup.add(KeyboardButton(anime))
            markup.add(KeyboardButton("Back"))
            bot.send_message(message.chat.id, "Choose Anime 👇", reply_markup=markup)

        # Anime → Season
        elif text in ANIME:
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for season in ANIME[text]:
                markup.add(KeyboardButton(f"{text} {season}"))
            markup.add(KeyboardButton("Back"))
            bot.send_message(message.chat.id, "Select Season 👇", reply_markup=markup)

        # 🎬 Send Anime File
        elif text in DATA:
    	    for ep in DATA[text]:
                bot.send_video(message.chat.id, ep)
        # 🎥 Movies
        elif text == "Tamil Movies Collection":
            bot.send_message(message.chat.id, "🎬 Sending Movies...")
            for m in MOVIES:
                bot.send_video(message.chat.id, m)

        # 🔊 Dubbed Movies
        elif text == "Tamil Dubbed Movies Collection":
            bot.send_message(message.chat.id, "🔊 Sending Dubbed Movies...")
            for m in DUB_MOVIES:
                bot.send_video(message.chat.id, m)

        # 🔙 Back
        elif text == "Back":
            bot.send_message(message.chat.id, "Main Menu", reply_markup=main_menu())

        # ❓ Help
        elif text == "Help":
            bot.send_message(message.chat.id, "Use menu bro 😎")

        else:
            bot.send_message(message.chat.id, "❌ Unknown bro")

    except Exception as e:
        print("Error:", e)

# ▶️ RUN
print("Bot running...")
bot.infinity_polling()
