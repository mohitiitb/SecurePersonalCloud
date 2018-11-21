import pyAesCrypt

buffersize=64*1024


def encrypt_AES(file,password,save_as):
    pyAesCrypt.encryptFile(file,save_as, password, buffersize)


def decrypt_AES(file,password,save_as):
    pyAesCrypt.decryptFile(file,save_as, password,buffersize)
