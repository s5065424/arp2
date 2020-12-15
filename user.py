import socket
c = socket.socket()
c.connect(('local host',9999))
print(c.recv(1024))
