state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

# "The AddRoundKey step is straightforward: it XORs the current state with the current round key."
def add_round_key(s, k):
    result = []
    for srow, krow in zip(state, round_key):
        resultrow = []
        for x,y in zip(srow, krow):
            resultrow.append(x ^ y)
        result.append(resultrow)
    return result

def matrix2bytes(matrix):
    return bytes(sum(matrix, []))

print(matrix2bytes(add_round_key(state, round_key)))

