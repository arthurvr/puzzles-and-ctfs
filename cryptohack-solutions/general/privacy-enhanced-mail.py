# "Extract the private key d as a decimal integer from this PEM-formatted RSA key."

from Crypto.PublicKey import RSA

path = "/path/to/privacy_enhanced_mail.pem"
key = RSA.importKey(open(path).read())
print(key.d)
