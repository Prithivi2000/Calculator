from tkinter import *

root= Tk()
root.title("My Calculator")
root.geometry("380x550+200+100")
root.resizable(False, False)
#----------------------FUNCTIONS-------------------------------------



def enterNumber(x):
    if entry_box.get() == '0':
        if x== '.':
            entry_box.insert(1,'.')
        else:

            entry_box.delete(0,'end')
            entry_box.insert(0,str(x))
        dot = entry_box.get()
        last_dot = dot[-1:]
        if last_dot in ['.'] or dot[-2:] == "..":
            pass
    else:
        length = len(entry_box.get())
        entry_box.insert(length, str(x))


def enterOperator(x):
    if entry_box.get() != '0':
        length= len(entry_box.get())
        all_text= entry_box.get()
        last_char = all_text[-1:]

        if last_char in ['+', '-', '*', '/'] or all_text[-2:]=="**":
            pass
        else:
            entry_box.insert(length, btn_operator[x]['text'])
def funcClear():
    entry_box.delete(0,'end')
    entry_box.insert(0,'0')

result=0
history=[]
def funcEqual():
    content= entry_box.get()
    result= eval(content)
    entry_box.delete(0,'end')
    entry_box.insert(0,result)
    history.append(content)
    history.reverse()

    status.configure(text="History:"+ '|'.join(history[0:4]),font= 'verdana 10 bold')

def funcDel():
    length = len(entry_box.get())
    entry_box.delete(length-1, 'end')
    if length == 1:
        entry_box.insert(0,'0')
#--------------------ENTRY BOX----------------------------------------------


entry_box = Entry(font= 'verdana 14 bold', width=22, bd=10, justify= RIGHT)
entry_box.insert(0,'0')
entry_box.place(x=30,y=10)

btn_numbers=[]
for i in range(10):
    btn_numbers.append(Button(width=4, text= str(i), bd=6, command=lambda x=i:enterNumber(x) ))

btn_text = 1
for i in range(3):
    for j in range(0,3):
        btn_numbers[btn_text].place(x=30+j*90 , y=70+i*70)
        btn_text+=1
company_status = Label(root, text= '@TROUBLESHOOTERS   TECHNOLOGICAL \nSOLUTION@\n Creator:Prithivi Guha', relief=SUNKEN, height= 3,bd=5, width= 22,anchor=W, font= 'verdana 11 bold')
company_status.pack(side=BOTTOM, fill=X)

status = Label(root, text= 'History', relief=SUNKEN, height= 3,bd=5, anchor=W, font= 'verdana 11 bold')
status.pack(side=BOTTOM, fill=X)


#------------------OPERATOR BUTTONS--------------------------

btn_operator=[]

for i in range(4):
    btn_operator.append(Button(width=4, font='times 10 bold', bd=5, command= lambda x=i:enterOperator(x)))
btn_operator[0]['text']='+'
btn_operator[1]['text']='-'
btn_operator[2]['text']='*'
btn_operator[3]['text']='/'

for i in range(4):
    btn_operator[i].place(x=290, y= 70+i*70)
btn_clear = Button(width=7, text='C', font='times 15 bold', bd=5, command=funcClear)
btn_clear.place(x=25, y=340)

btn_equal = Button(width=6, text="=", font='times 15 bold', bd=5 ,command= funcEqual)
btn_equal.place(x=150 , y=340)

btn_dot = Button(width=6, text=".", font=' times 15 bold', bd=5, command= lambda x= '.':enterNumber(x))
btn_dot.place(x=250,y=340)

btn_zero = Button(width=14, text='0', bd=5, command= lambda x= 0:enterNumber(x))
btn_zero.place(x=25, y= 280)

btn_del = Button(width=8, text='DEL', font='times 15 bold', bd=5, command= funcDel)
btn_del.place(x=150, y=280)



root.mainloop()