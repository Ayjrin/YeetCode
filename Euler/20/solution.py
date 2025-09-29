# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 =
# 27.

# Find the sum of the digits in the number 100!
import time
import math


# Organic, artisanlly made factorial
def factorial(n: int) -> int:
    product = n
    while n > 0:
        product *= n
        n -= 1
    return product


# Home grown sum for some reason
def find_sum(n: int):
    summed_num = 0
    i = 0
    string = str(n)
    iterable_list = list(string)

    while i < len(iterable_list):
        summed_num += int(iterable_list[i])
        i += 1
    return summed_num


# Artisinal implementation with timing
start_time = time.time()
result_original = find_sum(factorial(100))
end_time = time.time()
print(f"Original time: {end_time - start_time:.6f} seconds")


# -------------------------------------------------------------------------------- #


# Optimized implementation bc C > Python
def optimized_sum_factorial_digits(n: int) -> int:
    factorial_result = math.factorial(n)
    return sum(int(digit) for digit in str(factorial_result))


# Optimized implementation with timing
start_time = time.time()
result_optimized = optimized_sum_factorial_digits(100)
end_time = time.time()
print(f"Optimized time: {end_time - start_time:.6f} seconds")


if result_optimized == result_original:
    print(result_optimized)
