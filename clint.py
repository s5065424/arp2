import socket
c = socket.socket()
c.connect(('127.0.0.1',9999))
print ("Enter ""A"" to increase by 40\n")
print ("Enter ""B"" to decrease by 40\n")
print ("Enter ""C"" to quit the program\n")
name = input("Enter your requirements\n")
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode)
