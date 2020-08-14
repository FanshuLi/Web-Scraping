import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters, InlineQueryHandler
import requests
import urllib2
import re
import flag


updater = Updater(token = '547490465:AAFkZ-iX4Xqoiqr_3sVIQKs6UyrJg05OKTA')

dispatcher = updater.dispatcher
delay = updater.job_queue

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

'''
help - command list
admin - admin list
rule - rules of this group
bmx - What is BMX and benefit of holding BMX
faq - Most asked questions
socialmedia - social media list
fee - Trading, deposit and withdrawal fee
bmxprice - What is the real-time price of BMX
announcement - Obtain the weekly reports and latest news
bmxamount - If you have any question about the amount of BMX you received
'''

def getPrice(coinType):
    url = "https://api.bitmart.com/api/v3/market_price_chart?coinType=%s" % coinType
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }
    resp = requests.session().get(url, headers = header)
    data = resp.json()['data']['result']
    result = []
    for i in data:
        tmp = re.findall("[0-9]*\.+[0-9]+", str(i['data']))
        if tmp:
            result.append(tmp[-1])
        else:
            result.append(0.0)
    return result

def getSymbolPrice(symbol):
    url = 'https://openapi.bitmart.com/v2/ticker?symbol=%s' % symbol
    response = requests.get(url).json()
    # bid = response['bid_1']
    # ask = response['ask_1']
    currentPrice = response['current_price']
    return (currentPrice)

def start(bot, job):
    bot.send_message(
        chat_id='@BitMartExchange',
        text=
        "Hi, I'm May.\nClick /help to see the commands. \nAnd if you have any questions, please submit a [ticket](https://support.bitmart.com/hc/en-us/requests/new).\nNew User Tutorial: [How to trade at BitMart](https://support.bitmart.com/hc/en-us/articles/360015440454-BitMart-Trading-Guide)\n[Birthday Gift](https://support.bitmart.com/hc/en-us/articles/360016261373-Free-Tokens-Sound-Better-Than-A-Birthday-Cake-BitMart-Announces-Birth-Month-Promotions-)",
        parse_mode=telegram.ParseMode.MARKDOWN,
        disable_web_page_preview=True)
# start_handler = CommandHandler('start',start)
# dispatcher.add_handler(start_handler)
delay.run_repeating(start, interval = 7200, first = 7200)

# def bitmartlove(bot, job):
#     bot.send_message(
#         chat_id='@BitMartExchange',
#         text=
#         "[BitMart Love. Be My Love.](https://support.bitmart.com/hc/en-us/articles/360017875193-BitMart-Love-Be-My-Love-)",
#         parse_mode=telegram.ParseMode.MARKDOWN,
#         disable_web_page_preview=True)
# delay.run_repeating(bitmartlove, interval = 86400, first = 59400)

def fee(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text="Details about trading, deposit and withdrawal [fee](https://support.bitmart.com/hc/en-us/articles/360002043633-Fees). And a reminder: if you want to withdraw your coins, do not withdraw to a contract address. And if you want to deposit Mobi or XLM, please remember that you must fill out the deposit address and the memo information provided by BitMart, or you may not see your balance in your account.", parse_mode = telegram.ParseMode.MARKDOWN, disable_web_page_preview = True)
fee_handler = CommandHandler('fee', fee)
dispatcher.add_handler(fee_handler)

def bmx(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text="What is BMX and the benefit of holding BMX, see details [here](https://support.bitmart.com/hc/en-us/articles/360003185273-About-BMX)\nContract address of BMX: 0x986EE2B944c42D017F52Af21c4c69B84DBeA35d8\nCheck it [here](https://support.bitmart.com/hc/en-us/articles/360003255213-Contract-Address)", parse_mode = telegram.ParseMode.MARKDOWN, disable_web_page_preview = True)
bmx_handler = CommandHandler('bmx', bmx)
dispatcher.add_handler(bmx_handler)

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="/rule: rules of this group.\n/admin: admin list.\n/socialmedia: social media list.\n/bmx: What is BMX and benefit of holding BMX\n/faq: Most asked questions.\n/announcement: Obtain the weekly reports and latest news.\n/bmxprice: What is the real-time price of BMX?\n/bmxamount: If you have question about the amount of BMX you received.\n/fee: Trading, deposit and withdrawal fee.")
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

def faq(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text="The most asked questions are listed [here](https://support.bitmart.com/hc/en-us/categories/360000172733-faq).", parse_mode = telegram.ParseMode.MARKDOWN, disable_web_page_preview = True)
faq_handler = CommandHandler('faq', faq)
dispatcher.add_handler(faq_handler)

def announcement(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text="Obtain the weekly reports and latest news [here] (https://support.bitmart.com/hc/en-us/categories/115000436413-Annoucements).", parse_mode = telegram.ParseMode.MARKDOWN, disable_web_page_preview = True)
announcement_handler = CommandHandler('announcement',announcement)
dispatcher.add_handler(announcement_handler)

def admin(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=
        "Please only contact and trust admin if you have any question @f_ken @venomousz @EricCristobal @eyommey @Javen_Lou @wliday @fsunman @MinhVN @stayhungry4 and our official bot is @BitMartEXBot. Don't trust fake admin or fake bot."
    )


admin_handler = CommandHandler('admin', admin)
dispatcher.add_handler(admin_handler)

def rule(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = "This is a English only group. Do not spam, Otherwise, you will be banned, deleted and reported to the system")
rule_handler = CommandHandler('rule', rule)
dispatcher.add_handler(rule_handler)

def socialmedia(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=flag.flagize(
        "[Twitter](https://twitter.com/BitMartExchange)\n[Facebook](https://www.facebook.com/bitmartexchange)\n[Reddit](https://www.reddit.com/r/bitmartexchange)\n[Medium](https://medium.com/@bitmart.exchange)\n[Steemit](https://steemit.com/@bitmart)\n[Bitcointalk](https://bitcointalk.org/index.php?action=profile;u=1376628;sa=showPosts)\n[Instagram](https://www.instagram.com/bitmart_exchange)\n[LinkedIn](https://www.linkedin.com/company/bitmart)\n[Weibo](https://weibo.com/u/6424218806)\nMulti-lanuguage telegram group:\n[Telegram-Channel](t.me/BitMartExchange_Channel)\n:US:-[English-Telegram](t.me/BitMartExchange)\n:CN:-[Chinese-Telegram](t.me/BitMart_China)\n:VN:-[Vietnam-Telegram](t.me/BitMartExchange_Vietnam)\n:JP:-[Japanese-Telegram](t.me/BitMartExchange_Japanese)\n:KR:-[SouthKorea-Telegram](t.me/BitMartExchange_SouthKorea)\n:IN:-[India-Telegram](t.me/BitMartExchange_India)\n:RU:-[Russia-Telegram](t.me/BitMartExchange_Russia)\n:ES:-[Spanish-Telegram](t.me/BitMartExchange_Spanish)\n:ID:-[Indonesia-Telegram](t.me/BitMartExchange_Indonesia)\n:PH:-[Philippines-Telegram](t.me/BitMartExchange_Philippines)\n:NG:-[Nigeria-Telegram](https://t.me/joinchat/GI-JPlCCfDLTDHb_YBKc6Q)\n:TR:-[Turkish-Telegram](https://t.me/Bitmart_Turkish)\n:IT:-[Italy-Telegram](https://t.me/bitmart_italy)\n:FR:-[France-Telegram](https://t.me/bitmart_france)\n:DE:-[German-Telegram](https://t.me/BitMartExchange_Germany)"),
        parse_mode=telegram.ParseMode.MARKDOWN,
        disable_web_page_preview=True)


socialmedia_handler = CommandHandler('socialmedia', socialmedia)
dispatcher.add_handler(socialmedia_handler)

def bmxprice(bot,update):
    priceETH = getSymbolPrice('BMX_ETH')
    priceBTC = getSymbolPrice('BMX_BTC')
    priceUSDT = getSymbolPrice('BMX_USDT')
    bot.send_message(chat_id = update.message.chat_id, text = "The real-time price of BMX is: \n" + str(priceETH) + " ETH.\n" + str(priceBTC) + " BTC.\n" + str(priceUSDT) + " USDT.\n" + "\nPlease check details on our [website](https://www.bitmart.com/).", parse_mode = telegram.ParseMode.MARKDOWN, disable_web_page_preview = True)
bmxprice_handler = CommandHandler('bmxprice', bmxprice)
dispatcher.add_handler(bmxprice_handler)

def bmxamount(bot,update):
    bot.send_message(chat_id = update.message.chat_id, text = "Under normal circumstances, you will get your BMX rewards within 7 days after registration or referral. If you did not receive your BMX, make sure you did not spam or use fake email addresses, especially those who has abnormal high referrals. If you have any problem, please email support@bitmart.com and tell us: \n1. Your Telegram username: \n2. BitMart Account Email: \n3. How much BMX have you received totally: \n4. How much BMX you think you lack: \n5. How many people have you referred:")
bmxamount_handler = CommandHandler('bmxamount', bmxamount)
dispatcher.add_handler(bmxamount_handler)

def unknown(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=
        "Hi, I'm May.\nClick /help to see the commands. \nAnd if you have any questions, please submit a [ticket](https://support.bitmart.com/hc/en-us/requests/new).\nNew User Tutorial: [How to trade at BitMart](https://support.bitmart.com/hc/en-us/articles/360015440454-BitMart-Trading-Guide)\n[Birthday Gift](https://support.bitmart.com/hc/en-us/articles/360016261373-Free-Tokens-Sound-Better-Than-A-Birthday-Cake-BitMart-Announces-Birth-Month-Promotions-)",
        parse_mode=telegram.ParseMode.MARKDOWN,
        disable_web_page_preview=True)


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
