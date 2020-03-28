import binascii
filename = 'test.png'
with open(filename, 'rb') as f:
    content = f.read()
msg = binascii.hexlify(content)
print (msg)