import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "PASTE_YOUR_TOKEN_HERE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("📂 Previous Year Papers", callback_data="papers"),
        InlineKeyboardButton("📰 Daily News PDFs", callback_data="news"),
        InlineKeyboardButton("✈️ Flight Info", callback_data="flight"),
        InlineKeyboardButton("🧾 Sarkari Job Alerts", callback_data="jobs"),
        InlineKeyboardButton("💹 Investment Tips", callback_data="invest")
    )
    bot.send_message(message.chat.id, "👋 Welcome! Choose a category below:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "papers":
        bot.send_message(call.message.chat.id, "📂 Select Exam: JEE Main, NEET, NDA etc. (Coming Soon)")
    elif call.data == "news":
        bot.send_message(call.message.chat.id, "📰 Fetching latest news PDFs... (Coming Soon)")
    elif call.data == "flight":
        bot.send_message(call.message.chat.id, "✈️ Enter flight number or city (Coming Soon)")
    elif call.data == "jobs":
        bot.send_message(call.message.chat.id, "🧾 Latest Sarkari Job Alerts:\n1. SSC CGL 2025\n2. NDA 2\n3. UPSC CDS 2")
    elif call.data == "invest":
        bot.send_message(call.message.chat.id, "💹 Today's Investment Tip:\nAvoid FOMO. Research before investing.")

print("🤖 Bot is running...")
bot.polling()
