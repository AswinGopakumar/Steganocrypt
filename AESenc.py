from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import sys


def encryption():
    # A safe place to store a key. Can be on a USB or even locally on the machine (not recommended unless it has been further encrypted)
    key_location = "E:\\my_key.bin"

    # Generate the key
    key = get_random_bytes(32)

    # Save the key to a file
    try:
        file_out = open(key_location, "wb")  # wb = write bytes
        file_out.write(key)
        file_out.close()
    except FileNotFoundError:
        print("Insert the usb drive")
        print("Encryption failed")
        sys.exit(1)

    # AES-CFB mode encryption
    output_file = 'encrypted.bin'
    data = open('cipher.txt', 'rb')
    data_from_file = data.read()
    data.close

    cipher = AES.new(key, AES.MODE_CFB)  # CFB mode
    # Only need to encrypt the data, no padding required for this mode
    ciphered_data = cipher.encrypt(data_from_file)

    file_out = open(output_file, "wb")
    file_out.write(cipher.iv)
    file_out.write(ciphered_data)
    file_out.close()
    print("byte cipher data", ciphered_data)
    print("cipher_data",cipher.iv.hex()+" "+ciphered_data.hex())
    return None
