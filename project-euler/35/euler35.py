def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

primes_under_1_000_000 = prime_sieve(1000000)

def shift_left(n):
    return int(str(n)[1:] + str(n)[:1])


def generate_cycles(n):
    count = 0
    while (n in primes_under_1_000_000) and count < len(str(n)):
        count += 1
        n = shift_left(n)
    return len(str(n)) == count


def contains_even(n):
    lijst = [int(i) for i in str(n) if int(i) % 2 != 0]
    return len(lijst) != len(str(n))


som = 1 + sum([1 for i in primes_under_1_000_000 if (not contains_even(i)) and generate_cycles(i)])
print(som)
