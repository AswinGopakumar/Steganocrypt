from contextlib import nullcontext
from multiprocessing.context import assert_spawning
from turtle import clear

#function to convert input string to ascii and then to binary
def stringtobin(s):
        #converting string to ascii list
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
        binToDna(binstr)

#function to convert binary string to DNA bases
def binToDna(bstr):
        outputStr = ''
        for start in range(0, len(bstr), 2):
                word = bstr[start:start+2]
                if word == '00': outputStr += 'A'
                elif word == '01': outputStr += 'T'
                elif word == '10': outputStr += 'C'
                elif word == '11': outputStr += 'G'
        print(outputStr)
        dnaToAscii(outputStr)

#converts dna to ascii list and multiply it with a factor
def dnaToAscii(dstr):
        factor = 7
        f_list = list()
        da_list = [ord(c) for c in dstr]
        print(da_list)
        for a in da_list:
                a = a*factor
                f_list.append(a)
        f_joined = " ".join(str(n) for n in f_list)
        print(f_joined)
        fwrite(f_joined)

def fwrite(dnaascii):
        with open("cipher.txt",'w',encoding = 'utf-8') as f:
                f.write(dnaascii)

s = input("Enter your secret messege: ")
stringtobin(s)



