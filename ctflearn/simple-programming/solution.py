file = open("data.dat", "r")

count = 0

for line in file.readlines():
    number_of_ones = line.count('1')
    number_of_zeroes = line.count('0')

    if number_of_ones % 2 == 0:
        count += 1
    elif number_of_zeroes % 3 == 0:
        count += 1

print(count)

file.close()
