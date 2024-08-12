given_file = open("output.txt", "r").read().splitlines()

for line in given_file:
    part1 = int(line[0:4], 2) ^ 0b0101
    part2 = int(line[4:8], 2) ^ 0b0101
    result = (part1 << 4) + part2
    print(chr(result), end='')