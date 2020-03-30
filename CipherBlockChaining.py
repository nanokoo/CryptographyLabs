#!/usr/bin/python3
from Crypto.Cipher import AES
from Crypto import Random
import base64
BLOCK_SIZE=16 
def encryption(plaintext,key):
	#initialize AES
	random = Random.new()
	iv = random.read(BLOCK_SIZE)
	aes = AES.new(key, AES.MODE_CBC, iv)
	
	pad = BLOCK_SIZE - len(plaintext) % BLOCK_SIZE
	plaintext += bytes([pad] * pad)
	
	
	ciphertext = iv + aes.encrypt(plaintext)
	
	return ciphertext
	
def decrypt(ciphertext,key):
	
	iv = ciphertext[:BLOCK_SIZE]
	aes = AES.new(key, AES.MODE_CBC, iv)
	
	
	plaintext = aes.decrypt(ciphertext[BLOCK_SIZE:])
	
	
	pad = plaintext[-1]
	if pad not in range(1,33):
		raise Exception()
	if plaintext[-pad:] != bytes([pad] * pad):
		raise Exception()
		
	#remove padding
	return plaintext[:-pad]
	
if __name__ == "__main__":
	plaintext = b'scout'
	random = Random.new()
	key = random.read(16)
	c = encryption(plaintext,key)
	print(decrypt(c,key))