import pyDes

password="ritikroongta"
if len(password)<24:
	while len(password)!=24:
		password=password+" "
else:
	password=password[0:24]
#image
# import os
# import io
# from PIL import Image
# from array import array

# def readimage(path):
#     with open(path, "rb") as f:
#         return bytearray(f.read())
# path="pp.jpeg"
# data = readimage(path)

# k=pyDes.triple_des(password, pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
# d=k.encrypt(data)
# with open("en_image.des",'wb') as f:
# 	f.write(d)
# e=k.decrypt(d)
# image = Image.open(io.BytesIO(e))
# image.save("out.jpeg")


# #txt
# data=""
# with open("inp.txt",'rb') as f:
# 	data=f.read()
# k=pyDes.triple_des(password, pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
# d=k.encrypt(data)
# with open("encrypt.des",'wb') as f:
# 	f.write(d)
# e=k.decrypt(d)
# with open("out.txt",'wb') as f:
# 	f.write(e)


#pdf
import PyPDF2 

data=""
pdfFileObj = open('elec_notes.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
numPages=pdfReader.numPages
for i in range(numPages):
	pageObj = pdfReader.getPage(i)
	data=data+pageObj.extractText()  
pdfFileObj.close() 

k=pyDes.triple_des(password, pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
d=k.encrypt(data)
with open("pdf.des",'wb') as f:
	f.write(d)
e=k.decrypt(d)
pdfWriter = PyPDF2.PdfFileWriter()
with open("des.pdf",'wb') as f:
	pdfWriter.write(d)