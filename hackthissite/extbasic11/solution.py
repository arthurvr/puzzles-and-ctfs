def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

given_number = 1065435274

for modfactor in range(1, 2000):
    number = pow(2, 32) * modfactor + given_number

    factors = [largest_prime_factor(number)]
    if factors[0] > 101:
        continue
    else:
        number = number // factors[0]
        while number != 1:
            l = largest_prime_factor(number)
            factors.append(l)
            number = number // l

    print("Prime factors: ")
    print(factors)
    print()

    break

translation_table_index = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
translation_table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("The password contained the following characters:")
print(list(map(lambda x: translation_table[translation_table_index.index(x)], factors)))