from telebot import types
import telebot.types
from telebot import TeleBot

bot = TeleBot('***')

#start
@bot.message_handler(commands=['start'])
def send_welcome(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                        text= ('Welcome to the telephone book bot.\n'
                               'Here are your options: \n'
                               
                               'For read the existing file enter /read \n'
                               'For export data in lines enter /export_lines \n'
                               'For export data in columns enter /export_columns \n'
                               'For import data enter /document \n'
                               'If you want this message to repeat enter /start \n'
                               'If you forget the command - enter /help \n'))


@bot.message_handler(commands=['read'])
def read(msg: telebot.types.Message):
    with open('phone_book.txt', 'r', encoding='utf-8'):
        bot.send_document(chat_id=msg.from_user.id, document=open('phone_book.txt', 'rb'))        


            

#Help sending us to command start
@bot.message_handler(commands=['help'])
def help(msg: telebot.types.Message):  
    bot.send_message(chat_id=msg.from_user.id,
                        text='To see your options again, enter /start \n')




#Import
@bot.message_handler(content_types=['document'])
def hello(msg: telebot.types.Message):
    file = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    msg.document.file_name = 'temp.txt'
    with open('temp.txt', 'wb') as f_out:
        f_out.write(downloaded_file)
    with open('temp.txt', "r", encoding='utf-8') as f, open('phone_book.txt', "a", encoding='utf-8') as g:
            g.writelines('\n')
            for line in f:
                if len(line) > 20:
                    g.writelines(line)
                    g.writelines('\n')
            if len(line) < 20:
                with open('temp.txt', encoding='utf-8') as k:
                    lines = k.readlines()
                with open('phone_book.txt', "a", encoding='utf-8') as l:
                    j = 0
                    lst1 = []
                    for each in lines:
                        if not each.__contains__(','):
                            if each != '\n':
                                lst1.append(each.replace("\n", ""))
                                j += 1
                                if j == 4:
                                    l.writelines(', '.join(lst1))
                                    l.writelines('\n')
                                    j = 0
                                    lst1 = []    



#export in columns
@bot.message_handler(commands=['export_columns'])
def exp_c(msg: telebot.types.Message):
    with open('phone_book.txt', encoding='utf-8') as f:
            lines = f.readlines()

    with open('phone_book_exp.txt', "w", encoding='utf-8') as g:
            for each in lines:
                if each.__contains__(','):
                    str = each.split(', ')
                    g.writelines('\n'.join(str))
                    g.writelines('\n')
    bot.send_message(chat_id=msg.from_user.id,
                        text='Phone book \n')
    bot.send_document(chat_id=msg.from_user.id, document=open('phone_book_exp.txt', 'rb'))    



#export in lines
@bot.message_handler(commands=['export_lines'])
def exp_l(msg: telebot.types.Message):
    with open('phone_book.txt', "r", encoding='utf-8') as f:
            with open('phone_book_exp.txt', "w", encoding='utf-8') as g:
                for line in f:
                    g.write(line)
    bot.send_message(chat_id=msg.from_user.id,
                        text='Phone book \n')
    bot.send_document(chat_id=msg.from_user.id, document=open('phone_book_exp.txt', 'rb'))  
      
      
     
bot.polling()       