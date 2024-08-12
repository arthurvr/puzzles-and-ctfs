def split(word):
    return [char for char in word]

wordlist = [l.strip('\n') for l in open("wordlist.txt").readlines()]
wordlist_sorted = [sorted(split(s)) for s in wordlist]

inputlist = [l.strip('\n') for l in open("input.txt").readlines()]
inputlist_sorted = [sorted(split(s)) for s in inputlist]

solutions = ""
for i in range(0, len(inputlist)):
	for j in range(0, len(wordlist)):
			if inputlist_sorted[i] == wordlist_sorted[j]:
				solutions += wordlist[j] + ","

print(solutions[:-1])
