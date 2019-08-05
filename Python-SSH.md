# SSH based on python
Use python3 to connect to remote server

# 1 Class implementation
The established session should be stable and available.
```python
import paramiko  
import re  
  
  
class ShellHandler:  
    def __init__(self, host, user, psw):  
         self.ssh = paramiko.SSHClient()  
         self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
         self.ssh.connect(host, username=user, password=psw, port=22)  
         channel = self.ssh.invoke_shell()  
         self.stdin = channel.makefile('wb')  
         self.stdout = channel.makefile('r')  
  
  
    def __del__(self):  
         self.ssh.close()  
  
  
    def execute(self, cmd):  
        stdin,stdout,stderr = self.ssh.exec_command(cmd)  
        msg = stdout.read(1024)  
        return msg.decode('utf-8')
```
# 2 Running code
```python
from helloWorld import *  
  
ssh = ShellHandler(host,username,passwd)  
  
while True:  
    command = str(input('Input command$ '))  
    print(ssh.execute(command))
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQxMjg3NTUxOV19
-->