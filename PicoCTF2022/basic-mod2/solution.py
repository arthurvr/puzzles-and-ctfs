input = open("message.txt", "r");
numbers = input.readline();

def inverse_mod_41(n):
    for i in range(41):
        if (n * i) % 41 == 1:
            return i

result = ""
for numstring in numbers.split():
    num = int(numstring) % 41
    num = inverse_mod_41(num)

    if num == 37:
        result += "_"
    elif num <= 25:
        result += "abcdefghijklmnopqrstuvwxyz"[num - 1]
    else:
        result += "0123456789"[num - 27]


print("picoCTF{" + result + "}")
