input = open("message.txt", "r");
numbers = input.readline();

result = ""
for numstring in numbers.split():
    num = int(numstring) % 37
    if num == 36:
        result += "_"
    elif num <=25:
        result += "abcdefghijklmnopqrstuvwxyz"[num]
    else:
        result += "0123456789"[num-26]

print("picoCTF{" + result + "}")


