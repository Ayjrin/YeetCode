# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

#notes:
# the quesetion really is how do you find a prime.

primes = []

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solve(target):
    candidate = 2
    while len(primes) <= target:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1

    print(primes[target-1])


solve(10_001)
