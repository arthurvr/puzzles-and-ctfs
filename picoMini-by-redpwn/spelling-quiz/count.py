frequencies = {}

alphabet = list('abcdefghijklmnopqrstuvwxyz')
for letter in alphabet:
    frequencies[letter] = 0

with open("public/study-guide.txt") as f:
    data = f.read()
    data = "".join(data.split())
    for char in data:
        frequencies[char] += 1
    print(frequencies)
