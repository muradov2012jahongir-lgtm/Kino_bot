import telebot
from flask import Flask
from threading import Thread

# 1. Server yaratish (Render hostingi uchun)
app = Flask('')

@app.route('/')
def home():
    return "Bot yoniq!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. Botingiz Tokeni
TOKEN = "8409080639:AAGzCL-Hy8SRMI3fcNhh0zhr1EEL2ZCK1H8"
bot = telebot.TeleBot(TOKEN)

print("Bot muvaffaqiyatli ishga tushdi...")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f"Salom {message.from_user.first_name}!\nKino botga xush kelibsiz. Kino olish uchun kodni kiriting:")

@bot.message_handler(content_types=['text'])
def send_kino(message):
    kod = message.text.strip()
    
    if kod == "100":
        bot.send_message(message.chat.id, "🎬 **Forsaj 10 (Uzbek tilida)**\n\n🍿 Kino linki: https://t.me/SizningKanaliz/10")
    elif kod == "200":
        bot.send_message(message.chat.id, "🎬 **O'rgimchak odam**\n\n🍿 Kino linki: https://t.me/SizningKanaliz/11")
    else:
        bot.send_message(message.chat.id, "❌ Afsuski, bu kod bilan kino topilmadi. Kodni to'g'ri kiritganingizni tekshiring.")

# 3. Mana shu oxirgi qismini ham to'liq ko'chiring:
if __name__ == "__main__":
    keep_alive()
    bot.remove_webhook()
    bot.polling(none_stop=True)
