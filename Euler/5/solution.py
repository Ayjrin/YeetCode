# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# this is the least common multiple of the set {1,...20}
# lcm = (a * b) / gcd
# we find the gcd with the euclidian algo -- gcd(a, b) then mod b and be becomes a and we call gcd recursively with the new numbers.

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return abs(a * b) / gcd(a, b)

def solution(n):
    if (n == 1):
        return 1
    else:
        return lcm(n, solution(n-1))

print(int(solution(20)))
