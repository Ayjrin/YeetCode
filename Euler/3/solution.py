# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
#
# Thought process
# How do i make sure something is a factor?
# how do i make sure something is prime? -- i dont want to divide by everything below it. i guess i have to % half and below as a start.
# start at 2 work our way up until we can get to x % y == 0
# BT left is going to be x
# to get right, we need to do y / x = right
# then we can prime factor the right
# i think we do this recursivley until we get to the end. This can run into some memory issues even though a binary tree is O(n)
#
import math


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


class PrimeTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        if is_prime(value):
            return
        squirt = int(math.sqrt(value))

        for i in range(2, squirt + 1):
            if value % i == 0:
                if is_prime(i):
                    self.left = i

                    quotient = value // i
                    self.right = PrimeTree(quotient)
                    if is_prime(quotient):
                        print(quotient)

                    if not is_prime(quotient):
                        self.right.insert(quotient)
                break



prime = PrimeTree(600851475143)
prime.insert(prime.value)
