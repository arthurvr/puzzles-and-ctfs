import sys

# Found the right code in the program by looking for the "Name input: " string using Ghidra. The 
# formula for the right password depends on the name length, and is in the code pretty much
# literally (if you use the disassembled view).

input = sys.argv[1]

if len(input) == 1:
    print("The correct key is " + str(ord(input[0])))

if len(input) == 2:
    print("The correct key is " + str(ord(input[0]) * ord(input[1])))

if len(input) == 3:
    result = ((ord(input[1]) + ord(input[0])) * ord(input[2]) - ord(input[0])) * ord(input[2])
    print("The correct key is " + str(result))

if len(input) >= 4:
    print("Long names aren't implemented yet. Couldn't be bothered 😊")
