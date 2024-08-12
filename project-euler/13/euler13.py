numbers = map(int, open("numbers.txt").readlines())
print(str(sum(numbers))[:10])
