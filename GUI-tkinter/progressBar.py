from tkinter import *

from tkinter.ttk import Progressbar

from tkinter import ttk

window = Tk()

window.title("Welcome to progress app")

window.geometry('350x200')

step = 10
counter = 0
def counter_label(label):
  def count():
    global counter
    counter += step
    label.config(text=str(counter)+'%')
    if counter != 100:
        label.after(1000, count)
  count()

prog = 0
def counter_prog(bar):
  def count():
    global prog
    prog += step
    bar['value'] = prog
    if prog != 100:
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
