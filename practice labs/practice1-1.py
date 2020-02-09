import onetimepad

stringToBeEnvrypted = 'wiki'
res = ''.join(format(ord(i), 'b') for i in stringToBeEnvrypted) 
print(res)
key ='11110011'
seret = onetimepad.encrypt(res, key)
#encryptedBinary = ''.join(format(ord(i), 'b') for i in seret)
print(seret)
decryptedText= onetimepad.decrypt(seret, key)
print(decryptedText)