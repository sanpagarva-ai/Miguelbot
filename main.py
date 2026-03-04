
import telebot

TOKEN = "AQUI_VA_TU_TOKEN"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text.lower()
    
    if "hola" in texto:
        bot.reply_to(message, "Hola mi amor 💛 ¿Cómo estás?")
    elif "te extraño" in texto:
        bot.reply_to(message, "Yo también te extraño muchísimo 🥺💛")
    elif "qué haces" in texto:
        bot.reply_to(message, "Pensando en ti siempre 😌💛")
    else:
        bot.reply_to(message, "Cuéntame más 😍")

print("Bot corriendo...")
bot.infinity_polling()
