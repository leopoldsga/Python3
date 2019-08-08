from tkinter import *


##Text update function
def text_update_server2():
    newText = '\n' + "Hello, vpp"
    serverText.insert(END, newText)
    #serverText.update()

def text_update_server():
    newText = '\n' + "Hello, kernel"
    serverText.insert(END, newText)
    #serverText.update()


##mainloop
root = Tk()
root.title('Demo')

chooseOneStack = IntVar()

newText = StringVar()
newText = "Hello, world"
serverText = Text(root)
serverText.insert(END, newText)
kButton = Radiobutton(root, text = 'On Kernel', variable = chooseOneStack, value = 1,command = text_update_server)
vButton = Radiobutton(root,  text = 'On VLS-VPP',variable = chooseOneStack, value = 2,command = text_update_server2)

## layout
kButton.pack()
vButton.pack()
serverText.pack()

root.mainloop()
