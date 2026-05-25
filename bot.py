# ============================================
# ROYAL FALCON TELEGRAM BOT
# ============================================

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# --------------------------------------------
# BOT START MESSAGE
# --------------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = """
🦅 Welcome to ROYAL FALCON AI

💻 Information Technology Company
🚀 Design • Development • AI

Commands:
/services
/contact
/social
/projects
/help
"""

    await update.message.reply_text(welcome_text)

# --------------------------------------------
# SERVICES
# --------------------------------------------

async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🔥 OUR SERVICES

🎨 UI/UX Design
💻 Web Development
📱 App Development
🤖 AI Solutions
🎬 Video Editing
🌐 Branding
📢 Digital Marketing
"""

    await update.message.reply_text(text)

# --------------------------------------------
# CONTACT
# --------------------------------------------

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📞 CONTACT DETAILS

📧 Email:
skcodex.in@gmail.com

📱 WhatsApp:
9840534233

🌐 Instagram:
@royalfalcon.tech
@royalfalcon.community
"""

    await update.message.reply_text(text)

# --------------------------------------------
# SOCIAL LINKS
# --------------------------------------------

async def social(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🌍 SOCIAL LINKS

📸 Instagram Tech:
https://www.instagram.com/royalfalcon.tech

👥 Instagram Community:
https://www.instagram.com/royalfalcon.community

📢 Telegram:
https://t.me/tamilanimepack

▶️ YouTube:
https://www.youtube.com/@Sk_Production_Offical
"""

    await update.message.reply_text(text)

# --------------------------------------------
# PROJECTS
# --------------------------------------------

async def projects(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🚀 PROJECT SHOWCASE

✔ Mobile App UI
✔ AI Tools
✔ Portfolio Website
✔ Branding Designs
✔ E-commerce Website
✔ SaaS Dashboard
"""

    await update.message.reply_text(text)

# --------------------------------------------
# HELP
# --------------------------------------------

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🤖 AVAILABLE COMMANDS

/services
/contact
/social
/projects
/help
"""

    await update.message.reply_text(text)

# --------------------------------------------
# AUTO REPLY
# --------------------------------------------

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_message = update.message.text.lower()

    if "hi" in user_message:
        await update.message.reply_text("👋 Welcome to Royal Falcon Technologies 🚀")

    elif "price" in user_message:
        await update.message.reply_text("💰 DM us on Instagram for pricing details.")

    elif "website" in user_message:
        await update.message.reply_text("🌐 We create premium futuristic websites.")

    elif "ai" in user_message:
        await update.message.reply_text("🤖 Falcon AI is under development 🔥")

    else:
        await update.message.reply_text("⚡ Royal Falcon AI received your message.")

# --------------------------------------------
# MAIN BOT SYSTEM
# --------------------------------------------

app = ApplicationBuilder().token("8396269559:AAHYJ-zUR4W4-Wz7D_tbJzm8ZBnaj8SIYhY").build()

# COMMANDS
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("services", services))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(CommandHandler("social", social))
app.add_handler(CommandHandler("projects", projects))
app.add_handler(CommandHandler("help", help_command))

# AUTO MESSAGE REPLY
app.add_handler(MessageHandler(filters.TEXT, auto_reply))

# RUN BOT
print("🦅 Royal Falcon AI Bot Running...")
app.run_polling()
