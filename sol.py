print("Enter ""A"" to increase by 40\n")
print("Enter ""B"" to decrease by 40\n")
print("Enter ""C"" to quit the program\n")

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

