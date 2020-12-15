import socket
c = socket.socket()
c.connect(('127.0.0.1',9999))
print ('y to move the crane forward')
print ('f to move the crane backward')
print ('s to stop the crane')
name = input("Enter your requirements\n")
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode)
