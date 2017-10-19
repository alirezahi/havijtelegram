import telebot
import urllib
from urllib.request import Request,urlopen
from telebot import types


token = '457388430:AAGVWHOUYzXl2i07YK_7Dw_sTvl7C5oxbxw'
bime_bot = telebot.TeleBot(token)


@bime_bot.message_handler(commands=['start','نوع پاسخگویی بات'])
def start_bot(message):
    try:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2)
        information = types.KeyboardButton('اطلاعات')
        third = types.KeyboardButton('بیمه ثالث')
        carbody = types.KeyboardButton('بیمه بدنه')
        markup.add(information)
        markup.add(third,carbody)
        msg = bime_bot.reply_to(message, 'چه درخواستی از بات دارید؟',reply_markup=markup)
        bime_bot.register_next_step_handler(msg, get_type)
    except:
        bime_bot.reply_to(message, 'ببخشید. الان در دسترس نیستم')


@bime_bot.message_handler()
def start_bot(message):
    try:
        if not message.text in ['اطلاعات','بیمه ثالث','بیمه بدنه']:
            chat_id = message.chat.id
            data = {'message':message.text,'action':''}
            u = Request('http://192.168.110.47:8000/chat/message/'+str(chat_id)+'/',urllib.parse.urlencode(data).encode())
            response = urlopen(u).read().decode()
            msg = bime_bot.reply_to(message, response)
    except:
        bime_bot.reply_to(message, 'ببخشید. الان در دسترس نیستم')


def get_type(message):
    try:
        chat_id = message.chat.id
        text_type = ''
        if message.text == 'اطلاعات':
            text_type = 'information'
        if message.text == 'بیمه ثالث':
            text_type = 'thirdparty'
        if message.text == 'بیمه بدنه':
            text_type = 'carbody'
        data = {'message':'','type':text_type,'action':''}
        u = Request('http://192.168.110.47:8000/chat/message/'+str(chat_id)+'/',urllib.parse.urlencode(data).encode())
        response = urlopen(u).read().decode()
        msg = bime_bot.reply_to(message, response)
    except:
        bime_bot.reply_to(message, 'ببخشید. الان در دسترس نیستم')



bime_bot.polling(none_stop=True)
