subtractive_combos = {
	"XXXX": "XL",
	"LXXXX": "XC",
	"VIIII": "IX",
	"IIII": "IV",
	"CCCC": "CD",
	"DCCCC": "CM"
}

def diff(number):
    result = number
    for x in subtractive_combos:
        result = result.replace(x, subtractive_combos[x])
    return len(number) - len(result)

improved_chars = sum([diff(line.strip()) for line in open('roman.txt')])
print(improved_chars)


