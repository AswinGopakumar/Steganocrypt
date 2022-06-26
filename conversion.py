from bz2 import compress
from contextlib import nullcontext
from multiprocessing.context import assert_spawning
from turtle import clear
import gzip
import AESenc
import binascii
# function to convert input string to ascii and then to binary


def stringtobin(s):
    # converting string to ascii list
    alist = [ord(c) for c in s]
    print(alist)
    # converting ascii to binary string
    binstr = ""
    ltob = [bin(list_item)[2:] for list_item in alist]
    for list_item in ltob:
        if len(list_item) % 2 != 0:
            list_item = "0"+list_item
            binstr = binstr + list_item
    print("binary string :", binstr)
    return binstr

# function to convert binary string to DNA bases


def binToDna(bstr):
    outputStr = ''
    for start in range(0, len(bstr), 2):
        word = bstr[start:start+2]
        if word == '00':
            outputStr += 'A'
        elif word == '01':
            outputStr += 'T'
        elif word == '10':
            outputStr += 'C'
        elif word == '11':
            outputStr += 'G'
    print("DNA bases :", outputStr)
    return outputStr

# converts dna to ascii list and multiply it with a factor


def dnaToAscii(dstr):
    factor = 7
    f_list = list()
    da_list = [ord(c) for c in dstr]
    print(da_list)
    for a in da_list:
        a = a*factor
        f_list.append(a)
    f_joined = " ".join(str(n) for n in f_list)
    print("dna to ascii :", f_joined)
    return f_joined

# writes the ciphertext to a text file


def fwrite(dnaascii):
    with open("cipher.txt", 'wb') as f:
        f.write(dnaascii)
        f.close()
    print("fwrite")
    return None
# compresses the message using gzip


def compression(ascString):
    compressed_value = gzip.compress(bytes(ascString, 'utf-8'))
    print("compression :", compressed_value.hex()) #converts byte to hex
    return compressed_value


s = input("Enter your secret messege: ")
bistr = stringtobin(s)
btd = binToDna(bistr)
dToA = dnaToAscii(btd)
compr = compression(dToA)
filewrite = fwrite(compr)

AESenc.encryption()
