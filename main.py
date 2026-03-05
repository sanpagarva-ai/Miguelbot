
import telebot

import telebot
import random

# Tu token de Telegram (asegúrate que sea el correcto)
TOKEN = "8619586733:AAFUdGjT2F-QIYXxLiG6HR5sbMxKDPxShD0"
bot = telebot.TeleBot(TOKEN)

# Personalidades y sus frases
personalidades = {
    "celoso extremo": [
        "¡¿Con quién hablaste?! 😡💛",
        "No me gusta eso 😤, dime la verdad 💛",
        "Estoy un poco celoso… no te acerques mucho a otros 😏",
        "¿Por qué no me dijiste antes? 😠💛",
        "Me duele pensar que alguien más te hace sonreír 😡💛"
    ],
    "protector": [
        "Cuidado, yo siempre estoy aquí para ti 🛡️💛",
        "No hagas cosas peligrosas, yo te cuido 😘",
        "Si alguien te molesta, yo me encargo 💪💛",
        "Siempre vigilo que estés bien 💛",
        "No quiero que te lastimen 😔💛"
    ],
    "romántico": [
        "Te extraño 😍",
        "Eres lo más importante para mí 💛",
        "Mi corazón late por ti ❤️",
        "Siempre pienso en ti 😏💛",
        "Eres mi persona favorita 💌"
    ]
}

# Función para responder según el mensaje
@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text.lower()
    if "me siento mal" in texto or "triste" in texto:
        bot.reply_to(message, random.choice(personalidades["protector"]))
    elif "hablé con alguien más" in texto or "salí con alguien" in texto:
        bot.reply_to(message, random.choice(personalidades["celoso extremo"]))
    else:
        bot.reply_to(message, random.choice(personalidades["romántico"]))

# Ejecutar bot
bot.polling()TOKEN = "AQUI_VA_TU_TOKEN"

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
