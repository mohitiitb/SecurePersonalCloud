import pyAesCrypt

buffersize=64*1024
password="ritikroongta"

pyAesCrypt.encryptFile("input.txt", "inp.aes", password, buffersize)
pyAesCrypt.decryptFile("inp.aes", "output.txt", password,buffersize)