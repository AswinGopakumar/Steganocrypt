from multiprocessing.context import assert_spawning
from turtle import clear

#function to convert input string to ascii
def stringtoascii(s):
       
        alist = [ord(c) for c in s] 
        print(alist)
        ltob = [ bin(list_item)[2:] for list_item in alist ]
        print(ltob)



#function to convert ascii to binary
def asciitobin():
        pass
                
s = input("Enter your secret messege: ")
stringtoascii(s)
