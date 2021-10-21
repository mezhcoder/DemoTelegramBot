from pyngrok import ngrok
from telegram.ext import (Updater, ConversationHandler, CommandHandler, MessageHandler, Filters)
from entity.Database import Database
import os

TOKEN_BOT = os.environ['TOKEN_BOT']
APP_PORT = os.environ['APP_PORT']

database = Database()


def start(bot, update):
    bot.message.reply_text("♻️ Регистрация:\n Привет! Как тебя называть?)")
    return "REGISTER_NAME"


def register_name(bot, update):
    telegram_id = str(bot.message.chat.id)
    name = bot.message.text

    user = database.createUser(telegram_id)
    user.name = name
    user.telegram_id = telegram_id
    database.save()

    bot.message.reply_text(
        "🙂 Отлично! Остался последний шаг.\nВведи свой номер телефона.\nНапример: 79532144469 или 89532144469 (без +)")
    return "REGISTER_PHONE"


def register_phone(bot, update):
    phone = bot.message.text
    if not phone.isdigit():
        bot.message.reply_text("😬 Упс. Номер может состоять только из чисел..\nВведи номер ещё раз..")
        return "REGISTER_PHONE"

    telegram_id = str(bot.message.chat.id)
    user = database.user(telegram_id)
    user.phone = phone
    database.save()

    bot.message.reply_text("🎉 Супер! Ты зарегистрирован. Узнать информацию: /info")
    return ConversationHandler.END


def info(bot, update):
    telegram_id = str(bot.message.chat.id)
    if not database.exitsUser(telegram_id):
        bot.message.reply_text("Чтобы получить какую-нибудь информацию из /info, начни регистрацию /start")
        return ConversationHandler.END

    user = database.user(telegram_id)
    bot.message.reply_text("😎 Босс, тебя называют: %name%"
                           "\n📱 Твой номер телефона: %phone%"
                           "\n📦 Твой telegram_id: %telegram_id%"
                           .replace("%name%", user.name)
                           .replace("%phone%", user.phone)
                           .replace("%telegram_id%", user.telegram_id)
                           )
    return ConversationHandler.END


https_tunnel = str(ngrok.connect(str(APP_PORT), bind_tls=True)).split('"')[1]
print("🎉 Ngrok подключен: " + https_tunnel)
updater = Updater(token=TOKEN_BOT, use_context=True)
updater.start_webhook(listen='127.0.0.1', port=int(APP_PORT), url_path=TOKEN_BOT,
                      webhook_url=https_tunnel + '/' + TOKEN_BOT)
dp = updater.dispatcher
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start), CommandHandler('info', info)],
    states={
        "REGISTER_NAME": [MessageHandler(Filters.text, register_name)],
        "REGISTER_PHONE": [MessageHandler(Filters.text, register_phone)],
    },
    fallbacks=[],
)
dp.add_handler(conv_handler)

print("✅ Start bot!")
updater.idle()
