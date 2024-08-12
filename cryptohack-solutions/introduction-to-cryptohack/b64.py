from base64 import b64encode

# Given hex string:
given = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# First decode it into bytes
decoded_bytes = bytes.fromhex(given)

# Then encode it into base64
result = b64encode(decoded_bytes)

print(result)

