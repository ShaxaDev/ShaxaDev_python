#1-test
from telebot import types
key = types.InlineKeyboardMarkup(row_width=1)
c = types.InlineKeyboardButton('A) 1', callback_data='A')
c1 = types.InlineKeyboardButton('B) -1', callback_data='B')
c2 = types.InlineKeyboardButton('C) 0', callback_data='C')
key.add(c, c1, c2)
#2-test
k = types.InlineKeyboardMarkup(row_width=1)
c = types.InlineKeyboardButton('A) int', callback_data='qul')
c1 = types.InlineKeyboardButton('B) str', callback_data='qol')
c2 = types.InlineKeyboardButton('c) float', callback_data='qolu')
k.add(c, c1, c2)
#3-test
k1 = types.InlineKeyboardMarkup(row_width=1)
j = types.InlineKeyboardButton('A)True', callback_data='p')
j1 = types.InlineKeyboardButton('B)False', callback_data='p1')
j2 = types.InlineKeyboardButton('C)Error', callback_data='p2')
k1.add(j, j1, j2)
#4-test
test= types.InlineKeyboardMarkup(row_width=1)
t = types.InlineKeyboardButton("A)<class 'type'>", callback_data='test0')
t1 = types.InlineKeyboardButton("B)<class 'class'>", callback_data='test1')
t2 = types.InlineKeyboardButton("C)<class 'str'>", callback_data='test2')
test.add(t, t1, t2)
#5-test
#savol:  n,m=10.0,10 print(n is m) ?
savol = types.InlineKeyboardMarkup(row_width=1)
t3 = types.InlineKeyboardButton("A)False", callback_data='test3')
t4 = types.InlineKeyboardButton("B)True", callback_data='test4')
t5 = types.InlineKeyboardButton("C)Error", callback_data='test5')
savol.add(t3,t4,t5)

#6-test
#savol: x,y=3,4 print(int.__add__(x,y))?
test2= types.InlineKeyboardMarkup(row_width=1)
t6 = types.InlineKeyboardButton("A)34", callback_data='test6')
t7 = types.InlineKeyboardButton("B)7", callback_data='test7')
t8 = types.InlineKeyboardButton("C)12", callback_data='test8')
test2.add(t6, t7, t8)
#7-savol
#savol x=[1,1,0]\nprint(any(x))
test3= types.InlineKeyboardMarkup(row_width=1)
t9= types.InlineKeyboardButton("A)True", callback_data='test9')
t10 = types.InlineKeyboardButton("B)False", callback_data='test10')
t11 = types.InlineKeyboardButton("C)Error", callback_data='test11')
test3.add(t9,t10,t11)
#8-savol print(8----8)?
test4 = types.InlineKeyboardMarkup(row_width=1)
t12 = types.InlineKeyboardButton("A)-8", callback_data='test12')
t13 = types.InlineKeyboardButton("B)Error", callback_data='test13')
t14 = types.InlineKeyboardButton("C)16", callback_data='test14')
test4.add(t12,t13,t14)

#10-savol y=[1,0,1]\nprint(all(y))
test5 = types.InlineKeyboardMarkup(row_width=1)
t15 = types.InlineKeyboardButton("A)False", callback_data='test15')
t16 = types.InlineKeyboardButton("B)Error", callback_data='test16')
t17 = types.InlineKeyboardButton("C)True", callback_data='test17')
test5.add(t15,t16,t17)
#print(1//2)
sh= types.InlineKeyboardMarkup(row_width=1)
sh0 = types.InlineKeyboardButton("A)0", callback_data='w')
sh1 = types.InlineKeyboardButton("B)0.5", callback_data='w1')
sh2 = types.InlineKeyboardButton("C)0.50", callback_data='w2')
sh.add(sh0,sh1,sh2)


   


























#start
mark = types.ReplyKeyboardMarkup(row_width=2)
a1= types.KeyboardButton('Python maqolalar📜')
a2 = types.KeyboardButton('Python kitoblar📚')
a3 = types.KeyboardButton('Python learning🌎')
a4=types.KeyboardButton('Bot info🔰')
    
a6=types.KeyboardButton('Py video dars🛡')
a7 = types.KeyboardButton('Pycharm⬇️')
a8=types.KeyboardButton('Python coder👨‍💻')
mark.add(a1,a2,a3,a7,a6,a4,a8)
#maqolalar
markup = types.ReplyKeyboardMarkup(row_width=3)
        #b=types.KeyboardButton('Python beginner')
b1= types.KeyboardButton('if-elif-else')
b2 = types.KeyboardButton('for')
b3= types.KeyboardButton('global va lokal')
b4=types.KeyboardButton('while')
b5=types.KeyboardButton('Numbers')
b6=types.KeyboardButton('String')
b7=types.KeyboardButton('list')
b8=types.KeyboardButton('set')
b9=types.KeyboardButton('dictionary')
b10=types.KeyboardButton('Tuple')
b11=types.KeyboardButton('⬅️orqaga')
b12=types.KeyboardButton('Bitwise operator')
b13=types.KeyboardButton('Funksiyalar')
b14=types.KeyboardButton('List comprehension')
markup.add(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b12,b13,b14,b11)
#telegram bot
q=types.ReplyKeyboardMarkup(row_width=2)
q1=types.KeyboardButton('1-qism')
q2=types.KeyboardButton('2-qism')
q3=types.KeyboardButton('3-qism')
q4=types.KeyboardButton('Serverga qo\'yish')
q5=types.KeyboardButton('⬅️back')
q.add(q1,q2,q3,q4,q5)
#py dars
z=types.ReplyKeyboardMarkup(row_width=2)
z1=types.KeyboardButton('Beginner')
z2=types.KeyboardButton('Django')
z3=types.KeyboardButton('Tkinter')
z5 = types.KeyboardButton('Telegram bot yasash🤖')
z4=types.KeyboardButton('⬅️orqaga')
z.add(z1,z2,z3,z5,z4)

A=types.InlineKeyboardMarkup()
B=types.InlineKeyboardButton(text='python kanal',url='t.me/pythontestARXIV')
A.add(B)

o=types.ReplyKeyboardMarkup(row_width=2)
o1=types.KeyboardButton('Python boshlang\'ich')
o2=types.KeyboardButton('Python tkinter')
o3=types.KeyboardButton('Python telegram bot')
o4=types.KeyboardButton('⬅️orqaga')
o.add(o1,o2,o3,o4)
