#!/usr/bin/python3
from Crypto.Cipher import DES

def encryption(plaintext):
  k1 = b'-18Bkey-'
  cipher1 = DES.new(k1, DES.MODE_ECB)
  c1 = cipher1.encrypt(plaintext) #encrypt using k1

  k2 = b'-28Bkey-'
  cipher2 = DES.new(k2, DES.MODE_ECB)
  c2 = cipher2.decrypt(c1) #decrypt using k2

  k3 = b'-38Bkey-'
  cipher3 = DES.new(k3, DES.MODE_ECB)
  c3 = cipher3.encrypt(c2) #encrypt using k1
  return c3

def decryption(c3):
	k3 = b'-38Bkey-'
	cipher3 = DES.new(k3, DES.MODE_ECB)
	c2 = cipher3.decrypt(c3) #decrypt using k3
	
	k2 = b'-28Bkey-'
	cipher2 = DES.new(k2, DES.MODE_ECB)
	c1 = cipher2.encrypt(c2) #encrypt using k2
	
	k1 = b'-18Bkey-'
	cipher1 = DES.new(k1, DES.MODE_ECB)
	plaintext = cipher1.decrypt(c1) #decrypt using k1
	return plaintext
	
	

if __name__ == "__main__":
	msg = b'3timesDes'
	ciphertext = encryption(msg)
	plaintext = decryption(ciphertext)
	print(plaintext)