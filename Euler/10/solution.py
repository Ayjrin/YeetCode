# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def is_prime(n: int) -> bool:
    if n <= 1: # negative and 0 case
        return False
    if n <= 3: # 2 and 3 case
        return True
    if n % 2 == 0 or n % 3 == 0: # 2 and 3 multiple case which is the most common prime factors.
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6 # since we ruled out 2 and 3, we can just iterate by 6 to do a lil optemization here.
    return True

def solve(target):
    sum = 0
    for i in range(1, int(target)):
        if is_prime(i):
            sum += i
    print(sum)

solve(2_000_000)
