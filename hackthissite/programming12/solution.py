import re
import requests

# First, fetch the given challenge from the website:
url = "https://www.hackthissite.org/missions/prog/12/index.php"
cookies = {"HackThisSite":"rrumhg59tb76r1bil99e1np361"}

print("Making request")
r = requests.get(url, cookies=cookies)
m = re.search(r'String: \<\/b\>\<input type="text" value="(.+)"', r.text)
inp = m.group(1)
print("Given string: " + inp)

# Loop over the given string to find the prime sum and the composite sum, get the first 25 alphabetic characters as well.
primeSum = 0
compositeSum = 0
firstChars = ""
for char in inp:
	if char.isdigit():
		if char == '1' or char == '0': continue
		if char == '2': primeSum += 2
		if char == '3': primeSum += 3
		if char == '4': compositeSum += 4
		if char == '5': primeSum += 5
		if char == '6': compositeSum += 6
		if char == '7': primeSum += 7
		if char == '8': compositeSum += 8
		if char == '9': compositeSum += 9
	else:
		if len(firstChars) < 25:
			firstChars += char

# Calculate the product
prod = primeSum * compositeSum

# Increment these ASCII values by one:
newFirstChars = ""
for char in firstChars:
	newFirstChars += chr(ord(char) + 1)

# Solution
sol = newFirstChars + str(prod)
print("Solution: " + sol)

# Send it off and fingers crossed!
r = requests.post(url, cookies=cookies, data={'solution': sol, 'submitbutton': 'submit'}, headers={'referer':url})
if "Congrats" in r.text:
	print("Congrats! Succeeded mission!")
else:
	print("Did not succeed.")
	print(r.text)
