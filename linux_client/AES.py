import pyAesCrypt

buffersize=64*1024
<<<<<<< HEAD
password="ritikroongta"

pyAesCrypt.encryptFile("input.txt", "inp.aes", password, buffersize)
pyAesCrypt.decryptFile("inp.aes", "output.txt", password,buffersize)
=======


def encrypt_AES(file,password,save_as):
    pyAesCrypt.encryptFile(file,save_as, password, buffersize)


def decrypt_AES(file,password,save_as):
    pyAesCrypt.decryptFile(file,save_as, password,buffersize)
>>>>>>> origin/master
