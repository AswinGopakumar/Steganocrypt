import numpy as np
from PIL import Image
import AESDecrypt
import gzip

def Decode(src):

    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$t3g0" in message:
        print("Hidden Message:", message[:-5])
        msg = message[:-5]
    else:
        print("No Hidden Message Found")
    return msg

output_loc = 'D:\\Steganocrypt\\Output_image\\steg.png'
msg = Decode(output_loc)
B_msg = bytes.fromhex(msg)

output_file = 'encrypted.bin'
file_out = open(output_file, "wb")
file_out.write(B_msg)
file_out.close()

def Extract(c_value):
    plain_string_again = gzip.decompress(c_value).decode('utf-8')
    print(plain_string_again)
    return plain_string_again

def AsciiToDna(asciiv):
    list_ascii = list()
    dna_list = list()
    factor = 7
    list_fascii = asciiv.split(' ')
    print(list_fascii)
    for i in list_fascii:
        asc = int(i)/factor
        list_ascii.append(int(asc))
    for i in list_ascii:
        dna_list.append(chr(i))
    print(dna_list)
    outputStr = ''
    for i in dna_list:
        if i == 'A':
            outputStr += '00'
        elif i == 'T':
            outputStr += '01'
        elif i == 'C':
            outputStr += '10'
        elif i == 'G':
            outputStr += '11'
    print(outputStr)
    return outputStr

def binToStr(bstr):
    n = 8
    bToa_list = list()
    bin_list = [bstr[i:i+n] for i in range(0, len(bstr), n)]
    print(bin_list)
    for i in bin_list:
        bToa_list.append(int(i, 2))
    print(bToa_list)
    plaintxt = ''.join(chr(i) for i in bToa_list) #ascii to string
    print(plaintxt)
    return None

compressed_value = AESDecrypt.Decrypt()
asciiv = Extract(compressed_value)
bstr = AsciiToDna(asciiv)
binToStr(bstr)

