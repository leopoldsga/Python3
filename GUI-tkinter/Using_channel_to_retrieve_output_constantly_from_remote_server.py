from tkinter import *
from paramiko import *
import time

host = '127.0.0.1'
port = 6666
usr = 'yournanme'
passwd = 'passwd'


def session_establish(host,port, usr, passwd):
    myTrans = Transport((host,port))
    myTrans.start_client()
    myTrans.auth_password(username=usr,password=passwd)
    myChannel = myTrans.open_session()
    myChannel.get_pty()
    myChannel.invoke_shell()
    return myChannel

##Text update function
def text_update_server():
    ## On kernel
    if chooseOneStack.get() == 1:
        kSession.send(str(kernelCmd.get()))
        time.sleep(1)
        text = kSession.recv(10240)
        print(kernelCmd.get())
        newText.set('\n' + text.decode())
        serverText.insert(END,newText.get())
    ## on Userspace
    elif chooseOneStack.get() == 2:
        vSession.send(vlsCmd.get())
        time.sleep(1)
        text = vSession.recv(10240)
        newText.set('\n' + text.decode())
        serverText.insert(END, newText.get())

##mainloop
root = Tk()
root.title('VPP Demo')


## Platform changed flag
## flag = 1 ===> kernel
## flag = 2 ===> Userspace
chooseOneStack = IntVar()

## kernel command as one string variable
kernelCmd = StringVar()
kernelCmd.set('ps aux | grep ssh'+'\n')

## Userspace command as one string variable
vlsCmd = StringVar()
vlsCmd.set('ifconfig'+'\n')

## Creat server text
newText = StringVar()
newText.set("Hello, world")
serverText = Text(root)
serverText.insert(END,newText.get())

## Kernel and Userspace session establishment and radiobutton
kSession = session_establish(host,port,usr,passwd)
vSession = session_establish(host,port,usr,passwd)
kButton = Radiobutton(root, text = 'On Kernel', variable = chooseOneStack, value = 1,command = text_update_server)
vButton = Radiobutton(root,  text = 'On Userspace',variable = chooseOneStack, value = 2,command = text_update_server)

## layout
kButton.pack()
vButton.pack()
serverText.pack()

root.mainloop()
