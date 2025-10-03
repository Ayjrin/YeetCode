# Problem 34
# ==========
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of
# their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


def factorial(n: int) -> int:
    if n == 0:
        return 1
    fact = n
    for i in range(1, n):
        fact *= i
    return fact


# Checks individual number for if it is a curio -- inneficcient do to recalculating each digit each pass.
# def is_curio(n: int):
#     digits = str(n)
#     sum_of_factorials = 0
#     for i in range(len(digits)):
#         sum_of_factorials += factorial(int(digits[i]))
#     return True if sum_of_factorials == n else False


def is_fast_curio(n: int):
    digits = str(n)
    sum_of_factorials = 0
    for digit_char in digits:
        sum_of_factorials += factorial_map[int(digit_char)]
    return sum_of_factorials == n


# Mathematical proof for upper bound:
# We are concerned with the sum of the factorials of the number's digits.
# This means that we have to have the largest possible set of digits have an added factorial greater than that of the lowest number we can make with that number of digits.
# This can be simply reasoned that an upper bound exists because we are increasing by an order of magnitude for our minimum number while our maximum number can only increase by an additive 9!
# Here is what I mean in math:
# For an n-digit number, maximum sum of factorials = n × 9! (all digits = 9)
# Minimum n-digit number = 10^(n-1)
# For curious numbers to exist: n × 9! ≥ 10^(n-1)
#
# A few examples:
# - 1-digit: smallest is 1 (but we use 0 for math: 10^0 = 1)
# - 2-digit: smallest is 10 = 10^1
# - 3-digit: smallest is 100 = 10^2
# - 4-digit: smallest is 1000 = 10^3
# - n-digit: smallest is 10^(n-1)

# When the inequality breaks is when we can determine the largest integer n:
# n=7: 7×9! = 7×362880 = 2,540,160 ≥ 10^6 = 1,000,000   -- does not break the inequality
# n=8: 8×9! = 8×362880 = 2,903,040 < 10^7 = 10,000,000  -- breaks the inequality
#
# Therefore, no 8-digit or higher curious numbers can exist
# Upper bound is 7×9! = 2,540,160

factorial_map = {i: factorial(i) for i in range(10)}
curious_numbers = []
for n in range(3, 2_540_161):
    if is_fast_curio(n):
        curious_numbers.append(n)

print("Curious numbers:", curious_numbers)
print("Sum of curious numbers:", sum(curious_numbers))
