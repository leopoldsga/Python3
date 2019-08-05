# SSH based on python
Use python3 to connect to remote server.

# 1 Preliminaries
## 1.1 exec_command
1. Each exec_command() would open one new channel of which the working directory would be the root of the user.

# 2 Class implementation
The established session should be stable and available.
```python
import paramiko
import os
import select
import sys

trans = paramiko.Transport(('10.67.118.170', 22))
trans.start_client()

'''
default_key_file = os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')
prikey = paramiko.RSAKey.from_private_key_file(default_key_file)
trans.auth_publickey(username='super', key=prikey)
'''
trans.auth_password(username='seagal', password='sga')
channel = trans.open_session()
channel.get_pty()
channel.invoke_shell()
while True:
    readlist, writelist, errlist = select.select([channel, sys.stdin,], [], [])
    if sys.stdin in readlist:
        input_cmd = sys.stdin.readline()
        channel.sendall(input_cmd)

    if channel in readlist:
        result = channel.recv(1024)
        if len(result) == 0:
            print("\r\n**** EOF **** \r\n")
            break
        sys.stdout.write(result.decode())
        sys.stdout.flush()

channel.close()
trans.close()
```

# 3 References
- [paramiko-SSHClient](http://docs.paramiko.org/en/2.4/api/client.html#paramiko.client.SSHClient)
- [paramiko-channel](http://docs.paramiko.org/en/2.4/api/channel.html)
- [paramiko-instance](https://www.cnblogs.com/linyfeng/p/8964753.html)
- [paramiko-exce_command](https://www.cnblogs.com/franknihao/p/6536255.html)
- [SSH-return-immediately](https://www.jianshu.com/p/8d1766c23523)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYwOTQyODg1LC0yMTcyMTc4NjIsMTE1Nj
cwMTU3OSwtMTI4MTU1NzUxNCwzMDQyNzk5NTIsLTE3MjI3ODE5
NzksNDU5MDg3NzEwLDE0MTI4NzU1MTldfQ==
-->