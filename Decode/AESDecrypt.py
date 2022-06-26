from Crypto.Cipher import AES

def Decrypt():
    input_file = 'encrypted.bin'
    path = 'E:\\my_key.bin'

    with open(path, 'rb') as f:
        key = f.read()
        f.close()
    file_in = open(input_file, 'rb')
    iv = file_in.read(16)
    ciphered_data = file_in.read()
    file_in.close()

    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    original_data = cipher.decrypt(ciphered_data) # No need to un-pad

    print(original_data.hex())
    return original_data