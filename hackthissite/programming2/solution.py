from PIL import Image
morse = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')', '': ''}

im = Image.open("PNG.png")

width, height = im.size

results = []
count = 0
last = 0
for i in range(0, width*height):
	if im.getpixel((i % width, i // width)):
		results.append(i - last)
		last = i

result = ''.join(chr(i) for i in results)

decoded = ""
for word in result.split(' '):
	decoded += morse[word]
print(decoded)
