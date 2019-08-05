# SSH based on python
Use python3 to connect to remote server.

# 1 Preliminaries
## 1.1 exec_command
1. Each exec_command() would open one new channel of which the working directory would be the root of the user.

# 2 Class implementation
The established session should be stable and available.
```python
#Author link: [Origin](https://www.jianshu.com/p/8d1766c23523)
import paramiko
import os
import select
import sys

remoteIP = '127.0.0.1'
port = 22

#Establish one socket
trans = paramiko.Transport((remoteIP,port))
#Negotiate a new SSH2 session as a client. This is the first step after creating a new 
#Transport. A separate thread is created for protocol negotiation.
trans.start_client()

#Login with ras key
'''
default_key_file = os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')
prikey = paramiko.RSAKey.from_private_key_file(default_key_file)
trans.auth_publickey(username='super', key=prikey)
'''

#login with password
#auth_password(_username_, _password_, _event=None_, _fallback=True_)
#Authenticate to the server using a password. The username and password are sent over an 
#encrypted link.
trans.auth_password(username='seagal', password='sga')

#open_session(_window_size=None_, _max_packet_size=None_, _timeout=None_)
#Request a new channel to the server, of type "session". This is just an alias for calling 
#open_channel with an argument of "session".
#open_channel(_kind_, _dest_addr=None_, _src_addr=None_, _window_size=None_, 
#_max_packet_size=None_, _timeout=None_)
#kind(the kind of channel requested (usually  "session",  "forwarded-tcpip",  "direct-tcpip", 
#or  "x11")
channel = trans.open_session()

#Request a pseudo-terminal from the server. This is usually used right after creating a client 
#channel, to ask the server to provide some basic terminal semantics for a shell invoked with 
#invoke_shell.
channel.get_pty()

#Request an interactive shell session on this channel. If the server allows it, the channel 
#will then be directly connected to the stdin, stdout, and stderr of the shell.
channel.invoke_shell()

while True:
	#Put stdin and channel into readlist.
	#select is aware of whether the status of stdin or channel is changed.
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
- [paramiko-Transport](http://docs.paramiko.org/en/2.6/api/transport.html)
- [paramiko-SSHClient](http://docs.paramiko.org/en/2.4/api/client.html#paramiko.client.SSHClient)
- [paramiko-channel](http://docs.paramiko.org/en/2.6/api/channel.html)
- [paramiko-instance](https://www.cnblogs.com/linyfeng/p/8964753.html)
- [paramiko-exce_command](https://www.cnblogs.com/franknihao/p/6536255.html)
- [SSH-return-immediately](https://www.jianshu.com/p/8d1766c23523)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg1MjgwNzc0MCwtMTgzMjQxMDQwMSwtMj
E3MjE3ODYyLDExNTY3MDE1NzksLTEyODE1NTc1MTQsMzA0Mjc5
OTUyLC0xNzIyNzgxOTc5LDQ1OTA4NzcxMCwxNDEyODc1NTE5XX
0=
-->