"""from tkinter import *
from functools import partial
win = Tk()
result = Label(win,text = "",bg="gray",width=50,fg = "black")
result.grid(row=0,column=0,columnspan=4)
rowNum = 0
colNum = 0
buttons = ["1","2","3","4","5","6","7","8","9","0","+","-","x","/","//","%","**","c","="]
def Calculator(letters):
    if letters == "c":
        result.config(text = "0")
    elif letters == "=":
        operate = eval(result.cget("txt"))
        result.config(text= str(operate))
    else: 
        textCatcher = result.cget('text')
        result.config(text = f"{textCatcher}{letters}")
for i in range(len(buttons)):
    Button(win,text = buttons[i],width=4,command=partial(Calculator,buttons[i])).grid(row=rowNum+1,column=colNum)
    colNum += 1
    if colNum>3:
        rowNum += 1
        colNum = 0
win.config(bg = "lightblue"),win.geometry('350x250+750+300'),win.mainloop()"""





from tkinter import *
from functools import partial
win = Tk()
res = Label(win,bg='black',fg='white',width=30,text='')
res.grid(row=0,column=0,columnspan=4)
row_n = 0
col_n = 0
btn_txt = ["1","2","3","4","5","6","7","8","9","0","+","-","*","/","//","%","**","c","="]
def function(letter):
    if letter == 'c':
        res.config(text = '0')
    elif letter == '=':
        res.config(text = eval(res.cget("text")))
    else:
        text_catcher = res.cget('text')
        res.config(text = f'{text_catcher}{letter}')
for i in range(len(btn_txt)):
    Button(win,text = btn_txt[i],width=4,command=partial(function,btn_txt[i])).grid(row=row_n+1,column=col_n)
    col_n += 1
    if col_n > 3:
        row_n += 1
        col_n = 0
win.config(bg = "lightblue"),win.geometry('215x250+750+300'),win.mainloop()