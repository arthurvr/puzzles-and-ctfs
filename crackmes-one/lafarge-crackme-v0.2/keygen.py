username_input = input("Enter the username: ")
username_input_length = len(username_input)

String2 = "_r <()<1-Z2[l5,^"
String2_length = len(String2)
String1 = String2

if username_input_length > String2_length:
	L = username_input_length
else:
	L = String2_length

v7 = 0
shouldContinue = True

while shouldContinue:
	ind = v7 % String2_length
	newChar = (ord(String1[ind]) ^ ord(username_input[v7 % username_input_length])) % 25 + 65
	v7 = v7 + 1
	shouldContinue = v7 < L
	String1 = String1[:ind] + chr(newChar) + String1[ind+1:]

String1 = '-'.join(String1[i:i+4] for i in range(0, len(String1), 4))
print("Valid password: " + String1)
