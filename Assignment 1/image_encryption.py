
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
# Generate random RSA Keys
keyPair = RSA.generate(8192)

# Separate public key
pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

# Separate private key

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

# transfer image to hex

filename = 'test.jpeg'
with open(filename, 'rb') as f:
    content = f.read()
msg = binascii.hexlify(content)


encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))


decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted) # show the decrypted image
data = binascii.a2b_hex(decrypted) # convert hex to image 
with open('image.jpeg', 'wb') as image_file:
    image_file.write(data)