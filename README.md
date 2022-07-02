# Steganocrypt

Steganocrypt is a combination of LSB-Steganography as well as AES encryption along with DNA encoding. In this project we first encoded the plaintext to its corresponding DNA bases and then compressed the result using g-zip and converted it to a ciphertext using AES-256 encryption technology.
## Note
The key will be generated to a USB-drive which will then be required for decrypting the message

## Packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary packages.

```bash
pip install -r requirements.txt
```

## Usage

- **Step 1:** Clone the repository
- **Step 2:** Go to the cloned folder and open with terminal 
- **Step 3:** Run conversion.py to encode the message 
- **Step 4:** Run Decode.py to decode the message

## Issues
- The usb should be named "E" without quotes

    eg. - ``` E:\\my_key.bin```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GPL](https://choosealicense.com/licenses/gpl-3.0/)
