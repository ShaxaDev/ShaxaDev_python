import telebot 
from telebot import types
from baza import *
from keyboard import *
from  PIL import Image,ImageDraw,ImageFont
import os
token = '1379080434:AAGlczOYVdhX0pE_FyLxaLF0ruMu2Pl3wsY'

bot = telebot.TeleBot(token)
start_text = '*Assalomu alaykum {} xush kelibsiz \nushbu bot @PythonTestUz jamoasinig rasmiy boti.\nBu bot orqali python dasturlash tilidan \nnazariy,videodarslarni olishingiz va qo\'shimcha tarzda /test command orqali bilimingizni sinab\nCERTIFICATE ni qo\'lga kiriting*'
#txt='hali men toliq ishga tushmadim savolingizni ushbu guruhda qoldiring'
w=[]
@bot.message_handler(commands=["test"])
def te(tx): 
    st = bot.get_chat_member(chat_id="@PythonTestUz",user_id=tx.from_user.id).status
    members = ['creator', 'administrator', 'member']
    if st in members:
       
        jpg=open('test.jpg','rb') 
        bot.send_photo(tx.chat.id,jpg,sertifikat,parse_mode='markdown')
        bot.send_message(tx.chat.id, '1-test\nprint(+-1)', reply_markup=key)
        jpg.close()
    else:
        a=types.InlineKeyboardMarkup(row_width=1)
        d=types.InlineKeyboardButton(text='Python testlar',url='https://t.me/PythonTestUz')
        a.add(d)
        bot.send_message(tx.chat.id,'Bot to`liq ishlashi uchun quyidagi kanalga a`zo bo`ling va \n<i>/start commandasini qaytdan yuboring!</i>',parse_mode='html',reply_markup=a)



q=[]
@bot.callback_query_handler(func=lambda c: True)
def callback_query(call):
    st = bot.get_chat_member(chat_id="@PythonTestUz",user_id=call.message.from_user.id).status
    members = ['creator', 'administrator', 'member']
    if st in members:

        data = call.data
        #2-test
        

        if data == "A":

            bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id, text="2-test\nprint(type(1/2)) ?", reply_markup=k)

        elif data == "B":
            q.append('ok')
            bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id, text="2-test\nprint(type(1/2)) ?", reply_markup=k)

        elif data == "C":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id, text="2-test\nprint(type(1/2)) ?", reply_markup=k)
        elif data == 'qul':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="3-test\nprint(0.1+0.2==0.3)?", reply_markup=k1)
        
        #3-savol
        elif data == 'qol':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="3-test\nprint(0.1+0.2==0.3)?", reply_markup=k1)
                
        elif data == 'qolu':
            q.append('ok')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="3-test\nprint(0.1+0.2==0.3)?", reply_markup=k1)

        elif data == 'p':
            

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='4-test\nprint(type(type)) ?',reply_markup=test)
        
            

        #4-savol  
        elif data == 'p1':
            q.append('ok')
            
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='4-test\nprint(type(type)) ?',reply_markup=test)
        
        elif data == 'p2':
            
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='4-test\nprint(type(type))',reply_markup=test)   
        #5-savol
        elif data=='test0':
            q.append('ok')
            

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='5-test\nn,m=10.0,10\nprint(n is m) ',reply_markup=savol)
        
        
        elif data=='test1':
            
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='5-test\nn,m=10.0,10\nprint(n is m) ',reply_markup=savol)
            
        elif data=='test2':
        
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='5-test\nn,m=10.0,10\nprint(n is m) ', reply_markup=savol)
        #6-savol    
        elif data=='test3':
            q.append(['ok'])
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='6-test\nx,y=3,4 print(int.__add__(x,y))',reply_markup=test2)
            
        elif data=='test4':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='6-test\nx,y=3,4 print(int.__add__(x,y))',reply_markup=test2)
            
        elif data=='test5':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='6-test\nx,y=3,4 print(int.__add__(x,y))',reply_markup=test2)
        #7-savol
        elif data=='test6':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='7-test\nx=[1,1,0]\nprint(any(x))',reply_markup=test3)
        elif data=='test7':
            q.append('ok')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='7-test\nx=[1,1,0]\nprint(any(x))',reply_markup=test3)
        elif data=='test8':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='7-test\nx=[1,1,0]\nprint(any(x))', reply_markup=test3)
        #8-savol
        elif data=='test9':
            q.append('ok')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='8-test\nprint(8----8)', reply_markup=test4)
        elif data=='test10':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='8-test\nprint(8----8)', reply_markup=test4)
        elif data=='test11':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='8-test\nprint(8----8)', reply_markup=test4)
        #9-savol
        elif data=='test12':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='9-test\ny=[1,0,1]\nprint(all(y))', reply_markup=test5)
        elif data=='test13':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='9-test\ny=[1,0,1]\nprint(all(y))', reply_markup=test5)
        elif data=='test14':
            q.append('ok')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='9-test\ny=[1,0,1]\nprint(all(y))', reply_markup=test5)
    #10-savol
        elif data=='test15':
            q.append('ok')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='10-test\nprint(1//2)', reply_markup=sh)
            
            
        elif data=='test16':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='10-test\nprint(1//2)', reply_markup=sh)
        
        elif data=='test17':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='10-test\nprint(1//2)', reply_markup=sh)
        elif data=='w':
            q.append('ok')
            if 6<=len(q)<=8:
            
                send = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='*Siz {} ta to\'g\'ri yechdingiz Ism familyangizni to\'liq kiriting  serifikatga yoziladi aks holda sertifikat berilmaydi\nP.S:orada probel bilan m.s:Salimov Anvar*'.format(len(q)), parse_mode='markdown')
                bot.register_next_step_handler(send,rasm2)
                q.clear()
            elif 9<=len(q)<=10:
                send = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*Siz {} ta to\'g\'ri yechdingiz Ism familyangizni to\'liq kiriting  serifikatga yoziladi aks holda sertifikat berilmaydi\nP.S:orada probel bilan  m.s:Salimov Anvar*'.format(len(q)),parse_mode='markdown')
                bot.register_next_step_handler(send,rasm)
                q.clear()

            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text='*Siz {} ta to\'g\'ri yechdingiz bu juda kam sertifikat olish uchun kamida 6 ta bolishi kerak*'.format(len(q)), parse_mode='markdown')
                q.clear()
        elif data=='w1':
            if 6<=len(q)<=8:
            
                send = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='*Siz {} ta to\'g\'ri yechdingiz Ism familyangizni to\'liq kiriting serifikatga yoziladi aks holda sertifikat berilmaydi\nP.S:orada probel bilan m.s:Salimov Anvar*'.format(len(q)), parse_mode='markdown')
                bot.register_next_step_handler(send,rasm2)
                q.clear()
            elif 9<=len(q)<=10:
                send = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*Siz {} ta to\'g\'ri yechdingiz Ism familyangizni to\'liq kiriting  serifikatga yoziladi aks holda sertifikat berilmaydi\nP.S:orada probel bilan m.s:Salimov Anvar*'.format(len(q)),parse_mode='markdown')
                bot.register_next_step_handler(send,rasm)
                q.clear()

            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text='*Siz {} ta to\'g\'ri yechdingiz bu juda kam serifikat olish uchun kamida 6 ta bolishi kerak*'.format(len(q)), parse_mode='markdown')
                q.clear()
        elif data=='w2':
            if 6<=len(q)<=8:
            
                send = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='*Siz {} ta to\'g\'ri yechdingiz Ism familyangizni to\'liq kiriting  serifikatga yoziladi aks holda sertifikat berilmaydi\nP.S:orada probel bilan m.s:Salimov Anvar *'.format(len(q)), parse_mode='markdown')
                bot.register_next_step_handler(send,rasm2)
                q.clear()
            elif 9<=len(q)<=10:
                send = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            text='*Siz {} ta to\'g\'ri yechdingiz Ism familyangizni to\'liq kiriting kiriting serifikatga yoziladi aks holda sertifikat berilmaydi\nP.S:orada probel bilan m.s:Salimov Anvar*'.format(len(q)), parse_mode='markdown')
                bot.register_next_step_handler(send,rasm)
                q.clear()

            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text='*Siz {} ta to\'g\'ri yechdingiz bu juda kam sertifikat olish uchun kamida 6 ta bolishi kerak*'.format(len(q)), parse_mode='markdown')
                q.clear()
    elif st not in members:
        a=types.InlineKeyboardMarkup(row_width=1)
        d=types.InlineKeyboardButton(text='Python testlar',url='https://t.me/PythonTestUz')
        a.add(d)
        bot.send_message(call.message.chat.id,'Bot to`liq ishlashi uchun quyidagi kanalga a`zo bo`ling va \n<i>/start commandasini qaytdan yuboring!</i>',parse_mode='html',reply_markup=a)

        
        
        

#sert_berish qismi        
def rasm2(message):
    t=message.text
    image=Image.open('sert_2.jpg')
    draw=ImageDraw.Draw(image)
    font1=ImageFont.truetype('Vogue.ttf',50)
    s=t.split()
    if len(s)==2: 
        p=300,300
        draw.text(p,t,'black',font1)
        image.save('user.jpg')
        qr=open('user.jpg','rb')
        bot.send_photo(message.chat.id,qr)
        qr.close()
    else:
        bot.send_message(message.chat.id,'ism va familyangiz yozilishi shart aks holda sertifikat ololmaysiz! qaytadan testni ishlang')
    
def rasm(message):
    
    t=message.text
    image=Image.open('sert_!.jpg')
    draw=ImageDraw.Draw(image)
    font1=ImageFont.truetype('Vogue.ttf',50)
    s=t.split()
    if len(s)==2: 
        p=300,300
        draw.text(p,t,'black',font1)
        image.save('user.jpg')
        qr=open('user.jpg','rb')
        bot.send_photo(message.chat.id,qr)
        qr.close()
    else:
        bot.send_message(message.chat.id,'ism va familyangiz yozilishi shart aks holda sertifikat ololmaysiz! qaytadan testni ishlang')
    

       
     

@bot.message_handler(commands=["start"])
def repeat(message):
    st = bot.get_chat_member(chat_id="@PythonTestUz",user_id=message.from_user.id).status
    members = ['creator', 'administrator', 'member']
    if st in members:
        bot.send_message(message.chat.id,start_text.format(message.from_user.first_name), reply_markup=mark,parse_mode='markdown')
    else:
        a=types.InlineKeyboardMarkup(row_width=1)
        d=types.InlineKeyboardButton(text='Python testlar',url='https://t.me/PythonTestUz')
        a.add(d)
        bot.send_message(message.chat.id,'Bot to`liq ishlashi uchun quyidagi kanalga a`zo bo`ling va \n<i>/start commandasini qaytdan yuboring!</i>',parse_mode='html',reply_markup=a)

@bot.message_handler(content_types=['text'])
def text(message):
    st = bot.get_chat_member(chat_id="@PythonTestUz",user_id=message.from_user.id).status
    members = ['creator', 'administrator', 'member']
    if st in members:

    
        if "Python maqolalar📜"==message.text:
            bot.send_message(message.chat.id, "Assalomu alaykum tanlang\nmaqola mavzusini tanlang:", reply_markup=markup)
        
        if 'raxmat'==message.text:
            bot.send_message(message.chat.id,'arzimaydi bizni kuzatib boring')
        if 'Telegram bot yasash🤖'==message.text:
            q=types.ReplyKeyboardMarkup(row_width=2)
            q1=types.KeyboardButton('1-qism')
            q2=types.KeyboardButton('2-qism')
            q3=types.KeyboardButton('3-qism')
            q4=types.KeyboardButton('Serverga qo\'yish')
            q5=types.KeyboardButton('⬅️back')
            q.add(q1,q2,q3,q4,q5)
            bot.send_message(message.chat.id,'Python dasturlash tilida telegram bot yashash darslariga xush kelibsiz!',reply_markup=q)
        if '1-qism'==message.text:
            bot.reply_to(message,'https://youtu.be/FYuDyGkKVm8')
        if '2-qism'==message.text:
            bot.reply_to(message,'https://youtu.be/Iw2g9_UFx14')
        if '3-qism'==message.text:
            bot.reply_to(message,'https://youtu.be/4z5ANIanAr8')
        if 'Serverga qo\'yish'==message.text:
            bot.reply_to(message,'https://youtu.be/GRe3_DbmEM8')
        if '⬅️back'==message.text:  
            bot.send_message(message.chat.id,'Video dars mavzusini tanlang:',reply_markup=z)

        if 'Python learning🌎'==message.text:
            bot.reply_to(message,sayt)
        
        if 'Bot info🔰'== message.text:
            bot.reply_to(message,matn)
        
        if 'Py video dars🛡'==message.text:
            
            bot.send_message(message.chat.id,'Video dars mavzusini tanlang:',reply_markup=z)
        

        if 'Beginner'==message.text:
            bot.reply_to(message,'https://t.me/pythontestarxiv/47')
            bot.send_message(message.chat.id,'Bu 1-dars qolganlari ushbu kanalda kanalga azo bo\'ling',reply_markup=A)

        if 'Django'==message.text:
            bot.reply_to(message,'https://t.me/pythontestarxiv/95')
            bot.send_message(message.chat.id,'https://t.me/pythontestarxiv/96')
            bot.send_message(message.chat.id,'https://t.me/pythontestarxiv/97')
            bot.send_message(message.chat.id,'https://t.me/pythontestarxiv/98')
            bot.send_message(message.chat.id,'https://t.me/pythontestarxiv/99')
            bot.send_message(message.chat.id,'https://t.me/pythontestarxiv/100')
        
        if 'Tkinter'==message.text:
            
            bot.reply_to(message,'https://t.me/pythontestarxiv/72')
            bot.send_message(message.chat.id,'https://t.me/pythontestarxiv/73')
            bot.send_message(message.chat.id,'https://t.me/pythontestarxiv/76')
            bot.send_message(message.chat.id,'https://t.me/pythontestarxiv/74')
            bot.send_message(message.chat.id,'https://t.me/pythontestarxiv/85')
            bot.send_message(message.chat.id,'Darslar davomi ushbu kanalda👉: @pythontestarxiv')
        
        if 'Python kitoblar📚'==message.text:
            bot.reply_to(message,'Kitob mavzusini tanlang:',reply_markup=o)

        if 'Python boshlang\'ich'==message.text:
            bot.reply_to(message,'https://t.me/PythonTestUz/61')
        if 'Python tkinter'==message.text:
            bot.reply_to(message,'https://t.me/pythontestarxiv/52')
        if  'Python telegram bot'==message.text:

            bot.reply_to(message,'https://t.me/pythontestarxiv/41')
    
        
        if 'for'==message.text:
            bot.reply_to(message,'https://telegra.ph/Python-For-sikl-operatoriFor-Loop-07-05')
        
        if 'if-elif-else'==message.text:
            bot.reply_to(message,'https://telegra.ph/Python-da-if-else-shart-operatorlari-06-26')

        if 'global va lokal'==message.text:
            bot.reply_to(message,'https://telegra.ph/Global-va-Lokal-ozgaruvchilar-06-24')
        
        if 'while'==message.text:
            bot.reply_to(message,"https://telegra.ph/Python-da-While-sikl-operatori-bilan-ishlash-07-18")

        if 'Numbers'==message.text:
            bot.reply_to(message,'https://telegra.ph/Pythonda-sonlarNumbers-06-15')
        
        if 'String'==message.text:
            bot.reply_to(message,'https://telegra.ph/Pythonda-satrlar-bilan-ishlashString-06-16')
        
        if 'list'==message.text:
            bot.reply_to(message,'https://telegra.ph/Pythonda-List-bilan-ishlash-06-17')
        
        if 'set'==message.text:
            bot.reply_to(message,'https://telegra.ph/Python-da-SetToplam-bilan-ishlash-06-21')
        
        if 'dictionary'==message.text:
            bot.reply_to(message,'https://telegra.ph/Pythonda-DictionaryLugat-bilan-ishlash-06-20')

        if 'Tuple'==message.text:
            bot.reply_to(message,'https://telegra.ph/Tuple-06-19')

        if 'Funksiyalar'==message.text:
            bot.reply_to(message,'http://telegra.ph/Pythonda-funksiya-03-13')
        if 'List comprehension'==message.text:
            bot.reply_to(message,'http://telegra.ph/List-comprehension-06-16')
        if 'Bitwise operator'==message.text:
            bot.reply_to(message,' http://telegra.ph/Bitvays-bitwise-operatorlari-06-07')

        if 'Pycharm⬇️'==message.text:
        
            bot.send_message(message.chat.id,'Pythonni dasturini birinchi o\'rnatib\nkeyin pycharmni o\'rnating https://t.me/pythontestarxiv/33 ')  
            
            bot.send_message(message.chat.id,'https://t.me/pythontestarxiv/24')

        if 'Python coder👨‍💻'==message.text: 

            a=types.InlineKeyboardMarkup()
            d=types.InlineKeyboardButton(text='bu yerni bosing',url='t.me/ShaxaDev')
            a.add(d)
            bot.send_message(message.chat.id,'python dasturchisi bilan bog\'lanish',reply_markup=a)   






        if '⬅️orqaga'==message.text:
            bot.send_message(message.chat.id,start_text.format(message.from_user.first_name), reply_markup=mark,parse_mode='markdown')
        
    else:
        a=types.InlineKeyboardMarkup(row_width=1)
        d=types.InlineKeyboardButton(text='Python testlar',url='https://t.me/PythonTestUz')
        a.add(d)
        bot.send_message(message.chat.id,'Bot to`liq ishlashi uchun quyidagi kanalga a`zo bo`ling va \n<i>/start commandasini qaytdan yuboring!</i>',parse_mode='html',reply_markup=a)



bot.polling()

                

        

