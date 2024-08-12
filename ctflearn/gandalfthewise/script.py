import base64

x = "xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p"
x_decoded = base64.b64decode(x)

y = "h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU"
y_decoded = base64.b64decode(y)

result = ""

for i in range(len(x_decoded)):
  result += chr(x_decoded[i] ^ y_decoded[i])

print(result)
