from contextlib import nullcontext
from multiprocessing.context import assert_spawning
from turtle import clear

#function to convert input string to ascii and then to binary
def stringtobin(s):
        #converting string to ascii
        alist = [ord(c) for c in s] 
        print(alist)
        #converting ascii to binary string
        binstr = ""
        ltob = [ bin(list_item)[2:] for list_item in alist ]
        for list_item in ltob:
                if len(list_item)%2 != 0:
                        list_item = "0"+list_item
                        binstr = binstr + list_item
        print(binstr)


s = input("Enter your secret messege: ")
stringtobin(s)


