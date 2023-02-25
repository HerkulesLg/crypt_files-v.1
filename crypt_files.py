import pyAesCrypt
import generator

psw = generator.rand_psw()
print(psw)
# encrypt
pyAesCrypt.encryptFile('file.txt', 'crypt.txt.aes', psw)
# decrypt
pyAesCrypt.decryptFile('crypt.txt.aes', 'dataout.txt', psw)
# read decrypt file
with open('dataout.txt', 'r') as file:
    print(file.read())

