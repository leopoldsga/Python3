from tkinter import *

from tkinter.ttk import Progressbar

from tkinter import ttk

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

counter = 0
def counter_label(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter)+'%')
    label.after(1000, count)
  count()

prog = 0
def counter_prog(bar):
  def count():
    global prog
    prog += 1
    bar['value'] = prog
    bar.after(1000, count)
  count()


style = ttk.Style()

style.theme_use('default')

style.configure("black.Horizontal.TProgressbar", background='black')

bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar.grid(column=0, row=0)
gress = Label(window)
gress.grid(column=1, row=0)
counter_prog(bar)
counter_label(gress)

window.mainloop()
