import pyAesCrypt

buffersize=64*1024
password="ritikroongta"

pyAesCrypt.encryptFile("video.mp4", "inp.aes", password, buffersize)
pyAesCrypt.decryptFile("inp.aes", "out_aes.mp4", password,buffersize)