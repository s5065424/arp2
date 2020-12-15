import socket
s = socket.socket()
print('server socket created')

s.bind(('127.0.0.1',9999))

s.listen(1)
print('waiting')

while True:
   c, addr = s.accept()
   name = c.recv(1024).decode()
   
   print('connected with clint', addr,name)
   
   c.send(bytes('connection secured','utf-8'))
   c.close()
