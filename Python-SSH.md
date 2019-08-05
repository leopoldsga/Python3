# SSH based on python
Use python3 to connect to remote server

# 1 Class implementation
The established session should be stable and available.
```python
import paramiko  
  
  
class ShellHandler:  
    def __init__(self, host, user, psw): 
		 #create one ssh instance and do some options
         self.ssh = paramiko.SSHClient()  
         self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
         
         #connect to remote host  
         self.ssh.connect(host, username=user, password=psw, port=22)
         
         #generate one new interactive shell on the remote host
         channel = self.ssh.invoke_shell()  

		 #Return a file-like object associated with this channel.
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

# 3 References
- [paramiko-SSHClient](http://docs.paramiko.org/en/2.4/api/client.html#paramiko.client.SSHClient)
- [paramiko-channel](http://docs.paramiko.org/en/2.4/api/channel.html)
- [paramiko-instance](https://www.cnblogs.com/linyfeng/p/8964753.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MjI3ODE5NzksNDU5MDg3NzEwLDE0MT
I4NzU1MTldfQ==
-->