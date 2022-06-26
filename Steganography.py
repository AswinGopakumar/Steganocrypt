#        LSB Steganography
# Reference: https://medium.com/swlh/lsb-image-steganography-using-python-2bbbee2c69a2

import numpy as np
from PIL import Image

def Encode(src, message, dest):

    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    message += "$t3g0"
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print("ERROR: Need larger file size")

    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1

        array=array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest)
        print("Image Encoded Successfully")

sourceImg = "D:\\Steganocrypt\\Original_image\\hut.png"
destImg = "D:\\Steganocrypt\\Output_image\\steg.png"
with open('encrypted.bin','rb') as f:
    message = f.read()
    f.close()
hexmessage = message.hex()
Encode(sourceImg,hexmessage,destImg)