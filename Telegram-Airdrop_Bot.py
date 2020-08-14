from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler,InlineQueryHandler,RegexHandler,MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from termcolor import colored
from telegram.ext import Updater, MessageHandler, Filters
import logging
############################### Bot ############################################

updater = Updater(token = '1020835667:AAHeTNLcDHmDHAEVMRJTBvZ0Hvgwp9yP3Po')
dispatcher = updater.dispatcher
delay = updater.job_queue

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

# def new_member(bot, update):
#     for member in update.message.new_chat_members:
#         if member.username == 'YourBot':
#             update.message.reply_text('Welcome!')

# # updater = Updater(token = '1000140645:AAE9ngn_Ymv1psYDZ96af6_YWZy3qb6zJ_4')
# # updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))
# updater.start_polling()
# updater.idle()

def start(bot, update):
    update.message.reply_text(
    text="❓ What is BitMart? \n \
      \n \
🌟 BitMart Exchange is a premier global digital asset trading platform, ranking among the top 10 crypto exchanges on CoinMarketCap. Officially operated on March 15, 2018, BitMart currently has over 850,000 registered users, with a daily trading volume of about 1 billion US dollars.\n \
        \n \
📰 BitMart is featured on several platforms like Nasdaq MarketSite, BuzzFeed, Cointelegraph, NewsBTC, CCN, and AMBCrypto. \n \
\n \
Please click * [Next] * to continue! ",parse_mode= 'Markdown',
reply_markup = {
    "keyboard": [[{"text":"Next"}]], 
    "resize_keyboard": True, 
    "one_time_keyboard": True
  })
    
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def journey(bot, update):
    update.message.reply_text(main_menu_message(),
                            reply_markup=main_menu_keyboard())

def callback_query(bot,update):
    user=update.callback_query.from_user
    cmd=update.callback_query.data
    bot.send_message(user.id, cmd)
    update.callback_query.answer('Congratulations!')
updater.dispatcher.add_handler(CallbackQueryHandler(callback_query))

def help(bot,update):
     update.message.reply_text(' 👋 Hi! Thanks for join! Please use * /start * start the journey 💃 \n \
Please use * /admin * to contact admin if you have any questions 🤔️ ',parse_mode= 'Markdown')

def admin(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=
        "Please only contact and trust admin if you have any question @f_ken @venomousz @EricCristobal @eyommey @Javen_Lou @wliday @jiaowang @jasonjiachen @fsunman @MinhVN @msoto1210 and our airdrop bot is @BitMart_Airdrop_Bot. Don't trust fake admin or fake bot."
    )


admin_handler = CommandHandler('admin', admin)
dispatcher.add_handler(admin_handler)

def hello(bot, update,user_data):
  if update.message.text=='Next':
    update.message.reply_text(main_menu_message(),reply_markup=main_menu_keyboard())
  else: 
    update.message.reply_text("Hi, we are happy to have you with us! Please use * /start * to start",parse_mode= 'Markdown')
    
    
updater.dispatcher.add_handler(MessageHandler(Filters.text,hello,pass_user_data=True))

def main_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())

# # and so on for every callback_data option
# def first_submenu(bot, update):
#   pass

# def second_submenu(bot, update):
#   pass

############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton(' 💬 Join our Telegram Group 💬 ', callback_data='m1',url='https://t.me/BitMartExchange')],
              [InlineKeyboardButton('🔔 Join our Telegram Channel 🔔', callback_data='m2',url='https://t.me/BitMartExchange_Channel')],
              [InlineKeyboardButton('🕊 Follow our Twitter and retweet the pinned post 🕊', callback_data='m3',url='https://twitter.com/BitMartExchange')],
              [InlineKeyboardButton('📘 Follow our Facebook Page and share the pinned post 📘 ', callback_data='m4',url='https://www.facebook.com/bitmartexchange')],
              [InlineKeyboardButton('🌐 Sign up on the BitMart website 🌐', callback_data='m5',url='https://www.bitmart.com/register')],
              [InlineKeyboardButton('💰 Trade to unlock extra 20 BMX 💰 ', callback_data='m6',url='https://www.bitmart.com/trade/en')],
              [InlineKeyboardButton('👬 Invite friends with your referral code 👬 ', callback_data='hello',url='https://www.bitmart.com/invitation')],
              [InlineKeyboardButton('🗳︎ Submit your data 🗳︎',callback_data='💰Congrats! Rewards will be sent to you in 30 days 💰')]]
  return InlineKeyboardMarkup(keyboard)


############################# Messages #########################################
def main_menu_message():
  return '👍 Thank you, let’s start right away! \n \
      \n  Please finish the tasks below to get unlimited BMX rewards + 60% commissions! \n \
    \n \
✅ Join our Telegram Group and Telegram Channel (Mandatory: 10 BMX) \n \
      \n \
✅ Follow our Twitter and retweet the pinned post (Mandatory: 5 BMX) \n \
     \n \
✅ Follow our Facebook Page and share the pinned post (Mandatory: 5 BMX) \n \
        \n \
✅ Sign up on the BitMart website (Mandatory: 10 BMX) \n \
        \n \
✅ Trade to unlock extra 20 BMX (Optional: 20 BMX) \n \
          \n \
✅ Invite friends with your referral code (Optional: 10 BMX per referral + 60% commission)' 
 

############################# Handlers #########################################
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))

updater.start_polling()

updater.idle()