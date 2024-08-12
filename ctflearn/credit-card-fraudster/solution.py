import luhn

for i in range(5432100000001234, 5432109999991234, 10000):
    if i % 123457 == 0 and luhn.verify(str(i)):
        print("CTFlearn{{{}}}".format(i))
