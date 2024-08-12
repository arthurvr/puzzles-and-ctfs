# This is a manual decompiliation of the given dis.txt file.
# I mainly did it to understand the program, so it might not be 100% correct :)
# ============================================================================

def func2(x,y):
    return x^y

def func():
    fp = open('flag.txt').read()
    cipher = ''
    # Not sure these calls always translate to a for loop? .. this seemed like the most logical program
    for i in range(len(fp)):
        temp = func2(ord(fp[i]), 170)
        cipher += chr(func2(temp, i))

    print(cipher)
    f = open('encrypted_flag.txt', 'w')
    f.write(cipher)

# Lots of cleanup after this?
# ============================================================================

# The given output:
output = "éÿîÅËÎÞÃÙóÙÕÎÈÊúèÞÎÜÌÌÕÓÕìùÂéçÆÐþÿñÖËîÿôÿ"

# Let me try to do the inverse of the above functions?
result = ""
for i in range(len(output)):
    x = func2(ord(output[i]), i)
    x = func2(x, 170)
    result += chr(x)

print(result)

