import telepot
from decouple import config

bot = telepot.Bot(config("TELEGRAM_BOT_TOKEN"))
bot_name = "shop_notificator"
bot_username = "shopblog_bot"


def get_chat_ids():
    chat_ids = set()
    update_data = bot.getUpdates()
    for data in update_data:
        chat_ids.add(data["message"]["chat"]["id"])

    return list(chat_ids)


def send_message(message):
    for id in chat_ids:
        bot.sendMessage(id, message)


def receive_messages():
    return bot.getUpdates()


chat_ids = get_chat_ids()
