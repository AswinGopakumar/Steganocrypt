from multiprocessing.context import assert_spawning
from turtle import clear

#function to convert input string to ascii and then to binary
def stringtobin(s):
        #converting string to ascii
        alist = [ord(c) for c in s] 
        print(alist)
        #converting ascii to binary
        ltob = [ bin(list_item)[2:] for list_item in alist ]
        print(ltob)


s = input("Enter your secret messege: ")
stringtoascii(s) 
