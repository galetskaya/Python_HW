from telebot import TeleBot
import telebot
from telebot import types

bot = TeleBot('***')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/ration")
    btn2 = types.KeyboardButton("/comprehensive")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Hi, {0.first_name}! I am a bot who performs as a calculator "
                                           "Please, choose the number types you will work with: /ration or /comprehensive".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=["ration"])
def handle_text(msg: telebot.types.Message):
        bot.send_message(msg.chat.id, text="Enter 2 numbers and the action in between, as: 23*25.6")
        bot.register_next_step_handler(callback=viev_calc, message=msg)


def viev_calc(msg: telebot.types.Message):
        bot.send_message(chat_id=msg.from_user.id, text=calc(msg.text))



def calc(text):
    try:
        res = 0
        if "+" in text:
            lst = text.split('+')
            res = float(lst[0])+float(lst[1])
            return res
        elif "-" in text:
            lst = text.split('-')
            res = float(lst[0])-float(lst[1])
            return res
        elif "*" in text:
            lst = text.split('*')
            res = float(lst[0])*float(lst[1])
            return res
        elif "/" in text:
            lst = text.split('/')
            res = float(lst[0])/float(lst[1])
            return res
        else:
            res = 'Incorrect entering, enter 2 numbers and the action in between, as: 2*3'
            return res
    except:
        res = 'I do not understand commas, switch those to dots please, as well, I can perform only 1 action'
        return res


@bot.message_handler(commands=["comprehensive"])
def handle_text(msg: telebot.types.Message):
        bot.send_message(msg.chat.id, text="Enter 2 comples numbers and the action in between,"
                                           " as: 23+25j - 6-24j (with space in between the actions)")
        bot.register_next_step_handler(callback=viev_calc2, message=msg)


def viev_calc2(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,  text=compreh(msg.text))


def compreh(text):
    res = None
    lst = text.split()
    if lst[1] == '-':
        res = complex(lst[0]) - complex(lst[2])
        return str(res)
    elif lst[1] == '+':
        res = complex(lst[0]) + complex(lst[2])
        return str(res)
    elif lst[1] == '/':
        res = complex(lst[0]) / complex(lst[2])
        return str(res)
    elif lst[1] == '*':
        res = complex(lst[0]) * complex(lst[2])
        return str(res)
    else:
        print('Incorrect entering')
@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(msg.from_user.id, 'Hey, I can calculate only 1 actiob '
                                       'that is why please enter 2 numbers and action in between, as 23*25.6' )
    bot.send_message(chat_id=msg.from_user.id, text=f'Result is: {calc(msg.text)}')


bot.polling(none_stop=True)