import telebot

bot = telebot.TeleBot("PUT_YOUR_BOT_TOKEN_HERE")

@bot.message_handler(func=lambda message: True)
def reply(message):
    text = message.text.lower()

    if "scene pack" in text:
        bot.send_message(message.chat.id, "🔥 Here your Scene Pack 👉 https://yourlink.com")

    else:
        bot.send_message(message.chat.id, "Type 'scene pack' bro")

bot.polling()
