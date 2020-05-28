from random import randint
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

hands = ['早', '中', '晚']
'''
emoji = {
    '早': '義大利麵',
    '中': '水餃',
    '晚': '滷肉飯'
}
e = {
    '早': '早餐',
    '中': '中餐',
    '晚': '晚餐'
}
'''
food = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

a = randint(0, 10)
emoji = {
    '早': food[a],
    '中': food[a],
    '晚': food[a]
    }

def start(bot, update):
    update.message.reply_text('請問要吃',
        reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton(e, callback_data = hand) for hand, e in e.items()   ]]))
           

def play(bot, update):
    try:
        mine = random.choice(hands)
        """yours = update.callback_query.data"""
        update.callback_query.edit_message_text('為您選擇  {}！'.format(emoji[mine]))
    except Exception as e:
        print(e)


updater = Updater('1179634598:AAECJp3xNHNW3uXrZ3wcbB34gQdJ9-Sdx5A')


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(play))


updater.start_polling()
updater.idle()
