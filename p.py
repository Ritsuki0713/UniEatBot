import random
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

hands = ['早', '中', '晚']
hand2 = ['要', '不要']

food = ['總匯三明治', '鮪魚三明治', '煙燻三明治', '起司蛋餅', '薯餅蛋餅', '鮪魚蛋餅', '起司蔥抓餅', '原味蔥抓餅', '火腿蔥抓餅',
         '炸煎餃', '薯餅', '漢堡', '肉鬆御飯糰', '鮪魚御飯糰', '鐵板麵', '蘑菇鐵板麵','海南鐵板麵', '麵包' ]
food2 = ['蜜汁叉燒飯', '黃金起司蛋包飯', '糖醋雞肉飯', '鐵板豬肉販', '打拋豬', '親子丼飯', '鍋燒麵', '酸辣粉',
          '酸辣麵', '豚骨拉麵','醬油拉麵', '涼麵', '韓式部隊鍋', '肌肉燴飯', '壽司', '烤肉', '小火鍋', '泡麵',
         '咖哩飯', '關東煮', '雙蘇番茄蝦仁炒飯', '肉絲炒飯', '總匯披薩', '海鮮披薩', '夏威夷披薩']

emoj = {
    
    '早':random.choice(food),
    '中': random.choice(food2),
    '晚': random.choice(food2)
    
    }
e = {
    '早': '早餐',
    '中': '中餐',
    '晚': '晚餐'
}
def start(bot, update):
    update.message.reply_text('請問要吃',
        reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton(e, callback_data = hand) for hand, e in e.items()]]))
           

def play(bot, update):
    try:
        mine = random.choice(hands)
        """yours = update.callback_query.data"""
        update.callback_query.edit_message_text('為您推薦  {}！'.format(emoj[mine]))
    except Exception as e:
        print(e)

drink = ['豆漿', '紅茶', '綠茶', '奶茶', '牛奶', '咖啡', '果汁', '仙草茶']
emoj2 = {
    
    'ok':random.choice(drink),
    'not ok':"好的，我知道了。"
    
}
e1 = {
    
    'ok':'要',
    'not ok':'不要'
}


def start2(bot, update):
    update.message.reply_text('請問要喝',
        reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton(e1, callback_data = hand) for hand, e1 in e1.items()]]))
           

def play2(bot, update):
    try:
        mine = random.choice(hand2)
        """yours = update.callback_query.data"""
        update.callback_query.edit_message_text('為您推薦  {}！'.format(emoj2[mine]))
    except Exception as e1:
        print(e1)

updater = Updater('1179634598:AAECJp3xNHNW3uXrZ3wcbB34gQdJ9-Sdx5A')


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(play))
updater.dispatcher.add_handler(CommandHandler('start2', start2))
updater.dispatcher.add_handler(CallbackQueryHandler(play2))

updater.start_polling()
updater.idle()
