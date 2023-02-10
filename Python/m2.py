# Program: Find prime factors of a natural number

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def find_prime_factors(num):
    prime_factors = []
    i, stop = 2, num + 1
    while i < stop:
        if num % i == 0 and is_prime(i):
            prime_factors.append(i)
            num = num // i
            i += 1
    return prime_factors


num = 69
prime_factors = find_prime_factors(num)
print("Prime Factors of", num, ":", prime_factors)
