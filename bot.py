import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import json
import threading
import time
from flask import Flask

# ================= CONFIG =================
BOT_TOKEN = "8729100545:AAH8VCIq31WKDuGkKIdfKxOGePxMDXTgL0I"
ADMIN_ID = 6396618197
CHANNEL_USERNAME = "@tamilanimepack"
bot = telebot.TeleBot(BOT_TOKEN)

# ================= FLASK =================
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
def auto_delete(chat_id, msg_id, delay=300):
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
        f"🔥 Welcome {message.from_user.first_name}\nJoin: {CHANNEL_USERNAME}",
        reply_markup=main_menu()
    )

# ================= UPLOAD =================
user_upload = {}
episode_count = {}

@bot.message_handler(func=lambda m: m.text and m.text.startswith("#add"))
def add(m):
    if m.from_user.id != ADMIN_ID:
        return

    text = m.text.replace("#add", "").strip()
    parts = text.split(" ")

    if len(parts) < 2:
        bot.reply_to(m, "❌ Use: #add Animation Name S1")
        return

    raw = parts[0].lower()

    if raw in ["movie","movies"]:
        category = "Movies"
    elif raw in ["anime","animation"]:
        category = "Animation"
    elif raw in ["dub","dubbed"]:
        category = "Dubbed"
    else:
        bot.reply_to(m, "❌ Wrong category")
        return

    name = parts[1]
    season = parts[2] if len(parts) > 2 else "S1"

    key = f"{name} {season}"

    user_upload[m.from_user.id] = {
        "category": category,
        "name": name,
        "season": season,
        "key": key,
        "files": [],
        "thumb": None
    }

    episode_count[m.from_user.id] = 0

    bot.reply_to(m, f"📤 Upload {name} {season}\nSend thumbnail + videos")

# ================= FILE =================
@bot.message_handler(content_types=['photo','video','document'])
def file(m):
    if m.from_user.id not in user_upload:
        return

    data_user = user_upload[m.from_user.id]

    # Thumbnail
    if m.photo:
        data_user["thumb"] = m.photo[-1].file_id
        return

    fid = m.video.file_id if m.video else m.document.file_id

    episode_count[m.from_user.id] += 1

    data_user["files"].append({
        "file_id": fid,
        "ep": episode_count[m.from_user.id]
    })

# ================= DONE =================
@bot.message_handler(commands=['done'])
def done(m):
    if m.from_user.id != ADMIN_ID:
        return

    if m.from_user.id not in user_upload:
        bot.reply_to(m, "❌ No upload")
        return

    info = user_upload.pop(m.from_user.id)

    if not info["files"]:
        bot.reply_to(m, "❌ No files uploaded")
        return

    data[info["key"]] = info
    save_data()

    episode_count.pop(m.from_user.id, None)

    bot.reply_to(m, f"✅ {info['key']} saved!")

# ================= DELETE =================
@bot.message_handler(func=lambda m: m.text and m.text.startswith("#delete"))
def delete(m):
    if m.from_user.id != ADMIN_ID:
        return

    name = m.text.replace("#delete","").strip().lower()

    found = None
    for k in data:
        if name in k.lower():
            found = k
            break

    if found:
        del data[found]
        save_data()
        bot.reply_to(m, f"🗑 {found} deleted")
    else:
        bot.reply_to(m, "❌ Not found")

# ================= SHOW CATEGORY =================
@bot.message_handler(func=lambda m: m.text in ["🎬 Movies","🎞 Animation","🌐 Dubbed"])
def show_cat(m):
    cat = m.text.split(" ")[1]

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    added = set()

    for k,v in data.items():
        if v["category"] == cat:
            added.add(v["name"])

    for i in added:
        markup.add(KeyboardButton(i))

    markup.add(KeyboardButton("🔙 Back"))
    bot.send_message(m.chat.id, "Choose 👇", reply_markup=markup)

# ================= SHOW SEASON =================
@bot.message_handler(func=lambda m: any(v["name"] == m.text for v in data.values()))
def show_season(m):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    for k,v in data.items():
        if v["name"] == m.text:
            markup.add(KeyboardButton(v["season"]))

    markup.add(KeyboardButton("🔙 Back"))
    bot.send_message(m.chat.id, "Choose Season 👇", reply_markup=markup)

# ================= SEND =================
@bot.message_handler(func=lambda m: any(m.text in k for k in data))
def send(m):
    for k,v in data.items():
        if m.text in k:
            for file in v["files"]:

                ep = file.get("ep",1)

                caption = f"""📺 {v['name']} {v['season']} - EP {ep}

🔥 Enjoy your watching buddy's 😎
📥 Forward to Saved Messages after download

⚠️ Auto delete in 5 mins due to
🚫 Copyright issue
"""

                msg = bot.send_video(
                    m.chat.id,
                    file["file_id"],
                    caption=caption,
                    thumb=v.get("thumb")
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
        bot.infinity_polling()
    except:
        time.sleep(5)
