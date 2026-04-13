import telebot
from telebot.types import ReplyKeyboardMarkup
import json, threading, time, os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 6396618197

bot = telebot.TeleBot(BOT_TOKEN)

# ---------------- DATA ----------------
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except:
    data = {
        "Movies": {},
        "Anime": {},
        "Dubbed": {}
    }

def save():
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

# ---------------- AUTO DELETE ----------------
def auto_delete(chat_id, msg_id, delay=300):
    def delete():
        time.sleep(delay)
        try:
            bot.delete_message(chat_id, msg_id)
        except:
            pass
    threading.Thread(target=delete).start()

# ---------------- MENU ----------------
def main_menu():
    m = ReplyKeyboardMarkup(resize_keyboard=True)
    m.add("🎬 Movies", "📺 Anime", "🌐 Dubbed")
    return m

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, "🔥 Welcome bro 😎", reply_markup=main_menu())

@bot.message_handler(func=lambda m: m.text == "🔙 Back")
def back(m):
    bot.send_message(m.chat.id, "Back 👇", reply_markup=main_menu())

# ---------------- CATEGORY ----------------
@bot.message_handler(func=lambda m: m.text in ["🎬 Movies","📺 Anime","🌐 Dubbed"])
def category(m):
    cat = m.text.replace("🎬 ","").replace("📺 ","").replace("🌐 ","")
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    for name in data[cat]:
        markup.add(name)

    markup.add("🔙 Back")
    bot.send_message(m.chat.id, f"{cat} list 👇", reply_markup=markup)

# ---------------- ADMIN ADD ----------------
upload = {}

@bot.message_handler(func=lambda m: m.text and m.text.startswith("#add"))
def add(m):
    if m.from_user.id != ADMIN_ID:
        return

    parts = m.text.split()

    if len(parts) < 3:
        bot.reply_to(m, "Format: #add Category Name [Season]")
        return

    cat = parts[1]
    name = parts[2]
    season = parts[3] if len(parts) > 3 else None

    upload[m.from_user.id] = {
        "cat": cat,
        "name": name,
        "season": season,
        "files": [],
        "thumb": None
    }

    bot.reply_to(m, "📤 Send thumbnail first, then videos")

# ---------------- RECEIVE FILE ----------------
@bot.message_handler(content_types=['photo','video','document'])
def file(m):
    if m.from_user.id not in upload:
        return

    if m.photo:
        upload[m.from_user.id]["thumb"] = m.photo[-1].file_id
    else:
        fid = m.video.file_id if m.video else m.document.file_id
        upload[m.from_user.id]["files"].append(fid)

# ---------------- DONE ----------------
@bot.message_handler(commands=['done'])
def done(m):
    if m.from_user.id != ADMIN_ID:
        return

    if m.from_user.id not in upload:
        return

    info = upload.pop(m.from_user.id)

    cat = info["cat"]
    name = info["name"]
    season = info["season"]

    if season:
        data[cat].setdefault(name, {})
        data[cat][name].setdefault(season, {
            "files": [],
            "thumb": info["thumb"]
        })
        data[cat][name][season]["files"].extend(info["files"])
    else:
        data[cat].setdefault(name, {
            "files": [],
            "thumb": info["thumb"]
        })
        data[cat][name]["files"].extend(info["files"])

    save()
    bot.reply_to(m, "✅ Saved with thumbnail")

# ---------------- DELETE ----------------
@bot.message_handler(commands=['delete'])
def delete(m):
    if m.from_user.id != ADMIN_ID:
        return

    name = m.text.replace("/delete","").strip()

    for cat in data:
        if name in data[cat]:
            del data[cat][name]
            save()
            bot.reply_to(m, f"🗑 {name} deleted")
            return

    bot.reply_to(m, "❌ Not found")

# ---------------- USER CLICK ----------------
@bot.message_handler(func=lambda m: True)
def handle(m):
    text = m.text

    for cat in data:
        if text in data[cat]:
            item = data[cat][text]

            if isinstance(item, dict) and "files" not in item:
                markup = ReplyKeyboardMarkup(resize_keyboard=True)
                for s in item:
                    markup.add(s)
                markup.add("🔙 Back")

                bot.send_message(m.chat.id, "Select Season", reply_markup=markup)
            else:
                send_files(m.chat.id, item, text)
            return

    for cat in data:
        for name in data[cat]:
            item = data[cat][name]

            if isinstance(item, dict) and text in item:
                send_files(m.chat.id, item[text], f"{name} {text}")
                return

    bot.send_message(m.chat.id, "❌ Use menu bro")

# ---------------- SEND FILES ----------------
def send_files(chat_id, item, title):
    files = item["files"]
    thumb = item.get("thumb")

    for i, f in enumerate(files, start=1):
        caption = f"🎬 {title} - EP{i}"

        video_msg = bot.send_video(
            chat_id,
            f,
            caption=caption,
            thumb=thumb
        )

        warn_msg = bot.send_message(
            chat_id,
            "⚠️ This video will be deleted in 5 minutes.\n📢 Save or watch now!"
        )

        auto_delete(chat_id, video_msg.message_id)
        auto_delete(chat_id, warn_msg.message_id)

# ---------------- RUN (FINAL FIX 🔥) ----------------
print("🔥 Bot running...")

while True:
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
