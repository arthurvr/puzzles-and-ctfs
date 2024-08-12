output = open('out', 'r').read()
solution = ""

for k in range(0xFFFD):
    for c in output:
        solution += chr((ord(c) - k) % 0xFFFD)

    if "flag" in solution:
        print(solution)
        solution = ""
    else:
        solution = ""
