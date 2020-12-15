import socket
s = socket.socket()
print('server socket created')

s.bind(('local host',9999))

s.listen(3)
print('connecting')

while True:

   c, addr = s.accept()
   print('connected with clint', addr)
val=0

while(1):
    inp = input("Enter the command ")
    if((inp=="A" or inp=="a")):
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

   c.send('done')
   c.lose()
