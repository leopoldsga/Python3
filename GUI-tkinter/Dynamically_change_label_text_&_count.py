#Dynamically change the text of one label and
#count the changed times.
#Author email: guoaosun@outlook.com

##Version 1-------------------------------------------
from tkinter import Tk, Checkbutton, Label,Radiobutton
from tkinter import StringVar, IntVar

root = Tk()

text = StringVar()
text.set('Hello, world')
status = IntVar()
counter  = StringVar()
cnt = 0
counter.set(str(cnt)+ " times")

def count():
    global counter, cnt
    cnt+=1
    counter.set(str(cnt) + " times")


def change():
    if status.get() == 1:   # if clicked
        text.set('Hello, Mack')
        count()
    else:
        text.set('Hello, Maria')
        count()

cb = Radiobutton(root, text = 'Mack',variable=status,value = 1, command=change)
cb2 = Radiobutton(root, text = 'Maria' ,variable=status, value =2, command=change)
lb = Label(root, textvariable=text, fg = 'green')
label = Label(root, textvariable = counter)
cb.pack()
cb2.pack()
lb.pack()
label.pack()

root.mainloop()
##--------------------------------------------------------------------

##Version 2-----------------------------------------------------------
from tkinter import Tk, Checkbutton, Label,Radiobutton
from tkinter import StringVar, IntVar

root = Tk()

text = StringVar()
text.set('Hello, world')
status = IntVar()
cnt = 0

def count():
    global label, cnt
    cnt+=1
    label.config(text = str(cnt) + " times")


def change():
    if status.get() == 1:   # if clicked
        text.set('Hello, Mack')
        count()
    else:
        text.set('Hello, Maria')
        count()

cb = Radiobutton(root, text = 'Mack',variable=status,value = 1, command=change)
cb2 = Radiobutton(root, text = 'Maria' ,variable=status, value =2, command=change)
lb = Label(root, textvariable=text, fg = 'green')
label = Label(root)
cb.pack()
cb2.pack()
lb.pack()
label.pack()

root.mainloop()
##--------------------------------------------------------------
