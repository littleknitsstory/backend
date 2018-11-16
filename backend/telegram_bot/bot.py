import telepot

bot = telepot.Bot('758746595:AAGLSnQNxRTewwgVSAnh2EvMnDTPMD1FZ5A')
bot_name = 'shop_notificator'
bot_username = 'shopblog_bot'


def get_chat_ids():
    chat_ids = set()
    update_data = bot.getUpdates()
    for data in update_data:
        chat_ids.add(data['message']['chat']['id'])

    return list(chat_ids)


def send_message(message):
    for id in chat_ids:
        bot.sendMessage(id, message)


def receive_messages():
    return bot.getUpdates()


chat_ids = get_chat_ids()


[
    {
        'update_id': 893100324,
        'message': {
            'message_id': 4,
            'from': {
                'id': 490331520,
                'is_bot': False,
                'first_name': 'Alexander',
                'username': 'r_avis',
                'language_code': 'en-GB'
            },
            'chat': {
                'id': 490331520,
                'first_name': 'Alexander',
                'username': 'r_avis',
                'type': 'private'
            },
            'date': 1542358110,
            'text': 'hi, bot!'
        }
    },
    {
        'update_id': 893100325,
        'message': {
            'message_id': 7,
            'from': {
                'id': 490331520,
                'is_bot': False,
                'first_name': 'Alexander',
                'username': 'r_avis',
                'language_code': 'en-GB'
            },
            'chat': {
                'id': 490331520,
                'first_name': 'Alexander',
                'username': 'r_avis',
                'type': 'private'
            },
            'date': 1542359121,
            'text': 'привет, ботелло! :)'
        }
    }
]
