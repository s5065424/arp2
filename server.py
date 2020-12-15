import socket
s = socket.socket()
print('server socket created')

s.bind(('127.0.0.1',9999))

s.listen(1)
print('waiting')

val=0

while True:
	c, addr = s.accept()
	name = c.recv(1024).decode()
	inp=name
	if((inp=="A" or inp=="a")):
	print('connected with clint', addr,name)
		if(val<=160):
			val+=40
			print("Value= ",val)
		else:
			print("Maximum limit 200 reached")
	elif((inp=="B" or inp=="b")):
		if(val>=40):
			val-=40
			print("Value= ",val)
		else:
			print("Minimum limit 0 reached")
	elif((inp=="C" or inp=="c")):
		print("Exiting program...")
		exit()
	else:
		print("Invalid command")
	c.send(bytes(('connection secured','utf-8'))
	c.close()
