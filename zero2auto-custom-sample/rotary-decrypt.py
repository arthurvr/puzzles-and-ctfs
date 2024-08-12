input = [ "F5gG8e514pbag5kg", ".5ea5/QPY4//", "pe51g5Ceb35ffn", "I9egh1/n//b3rk", "E5fh=5G8e514", "Je9g5Ceb35ffz5=bel", "I9egh1/n//b3", "E514Ceb35ffz5=bel", "t5gG8e514pbag5kg", ".5ea5/QPY4//", "F9m5b6E5fbhe35", "s9a4E5fbhe35n", "I9egh1/n//b3", "yb3.E5fbhe35", "yb14E5fbhe35" ]
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890./="

for inputstr in input:
    print(inputstr + ': \t\t' + ''.join([alphabet[(alphabet.index(char) + 13) % len(alphabet)] for char in inputstr]))
