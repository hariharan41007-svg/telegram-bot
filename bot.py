import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import json
import threading
import time
from flask import Flask

# ================= CONFIG =================
BOT_TOKEN = "8729100545:AAG3Dq7YNuLFFHvzRufC3-wgPlcI4xUJoxk"
ADMIN_ID = 6396618197 # 👉 unga Telegram ID
CHANNEL_USERNAME = "@tamilanimepack"

bot = telebot.TeleBot(BOT_TOKEN)

# ================= FLASK (Render fix) =================
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

def run_web():
    app.run(host="0.0.0.0", port=10000)

# ================= DATA =================
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except:
    data = {}

def save_data():
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

# ================= AUTO DELETE =================
def auto_delete(chat_id, msg_id, delay=300):  # 5 mins
    def delete():
        time.sleep(delay)
        try:
            bot.delete_message(chat_id, msg_id)
        except:
            pass
    threading.Thread(target=delete).start()

# ================= MENU =================
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("🎬 Movies"),
        KeyboardButton("🎞 Animation"),
        KeyboardButton("🌐 Dubbed")
    )
    return markup

# ================= START =================
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        f"🔥 Welcome {message.from_user.first_name}\n\nJoin: {CHANNEL_USERNAME}",
        reply_markup=main_menu()
    )

# ================= UPLOAD SYSTEM =================
user_upload = {}

# 👉 ADD COMMAND (SMART CATEGORY)
@bot.message_handler(func=lambda m: m.text and m.text.startswith("#add"))
def add_movie(m):
    if m.from_user.id != ADMIN_ID:
        return

    text = m.text.replace("#add", "").strip()

    if not text:
        bot.reply_to(m, "❌ Use: #add Movies Name")
        return

    parts = text.split(" ", 1)

    if len(parts) < 2:
        bot.reply_to(m, "❌ Use: #add Movies Name")
        return

    raw = parts[0].lower()

    if raw in ["movie", "movies"]:
        category = "Movies"
    elif raw in ["anime", "animation"]:
        category = "Animation"
    elif raw in ["dub", "dubbed"]:
        category = "Dubbed"
    else:
        bot.reply_to(m, "❌ Category must be Movies / Animation / Dubbed")
        return

    name = parts[1]

    user_upload[m.from_user.id] = {
        "category": category,
        "name": name,
        "files": [],
        "thumb": None
    }

    bot.reply_to(m, f"📤 Upload started for {name}\nSend thumbnail first, then videos")

# 👉 FILE RECEIVE (forward support)
@bot.message_handler(content_types=['photo','video','document'])
def receive_file(m):
    if m.from_user.id not in user_upload:
        return

    data_user = user_upload[m.from_user.id]

    # Thumbnail
    if m.photo:
        data_user["thumb"] = m.photo[-1].file_id
        return

    # Video / document (forward included)
    fid = None

    if m.video:
        fid = m.video.file_id
    elif m.document:
        fid = m.document.file_id

    if fid:
        data_user["files"].append(fid)

# 👉 DONE COMMAND
@bot.message_handler(commands=['done'])
def done_upload(m):
    if m.from_user.id != ADMIN_ID:
        return

    if m.from_user.id not in user_upload:
        bot.reply_to(m, "❌ No active upload")
        return

    info = user_upload.pop(m.from_user.id)

    if not info["files"]:
        bot.reply_to(m, "❌ No files uploaded")
        return

    name = info["name"]
    data[name] = info
    save_data()

    bot.reply_to(m, f"✅ {name} saved successfully!")

# ================= SHOW CATEGORY =================
@bot.message_handler(func=lambda m: m.text in ["🎬 Movies","🎞 Animation","🌐 Dubbed"])
def show_category(m):
    category = m.text

    if "Movies" in category:
        category = "Movies"
    elif "Animation" in category:
        category = "Animation"
    elif "Dubbed" in category:
        category = "Dubbed"

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    found = False
    for item in data:
        if data[item]["category"] == category:
            markup.add(KeyboardButton(item))
            found = True

    markup.add(KeyboardButton("🔙 Back"))

    if found:
        bot.send_message(m.chat.id, f"{category} list 👇", reply_markup=markup)
    else:
        bot.send_message(m.chat.id, "❌ No items found", reply_markup=markup)

# ================= SEND FILE =================
@bot.message_handler(func=lambda m: m.text in data)
def send_movie(m):
    item = data[m.text]

    for file_id in item["files"]:
        msg = bot.send_video(
            m.chat.id,
            file_id,
            caption=f"🎬 {m.text}\n\n⚠️ This video will be deleted in 5 minutes"
        )
        auto_delete(m.chat.id, msg.message_id)

# ================= BACK =================
@bot.message_handler(func=lambda m: m.text == "🔙 Back")
def back(m):
    bot.send_message(m.chat.id, "Main Menu", reply_markup=main_menu())

# ================= RUN =================
print("🔥 Bot running...")

threading.Thread(target=run_web).start()

while True:
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(e)
        time.sleep(5)
