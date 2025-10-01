# Surprisingly there are only three numbers that can be written as the sum
# of fourth powers of their digits:

#   1634 = 1^4 + 6^4 + 3^4 + 4^4
#   8208 = 8^4 + 2^4 + 0^4 + 8^4
#   9474 = 9^4 + 4^4 + 7^4 + 4^4

# As 1 = 1^4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth
# powers of their digits.


# Notes:
# how do we know when to stop?
#
# the largest nmber we can have is   d * 9^p   where p is the power and d is the number of digits.
# the smallest number we can have is   10^(d-1)
# we should stop when the max possible sum becomes smaller than the minimuim d-digit number.
# Proof for p = 5
# # 9^5 = 59,049 (maximum contribution per digit)
#
# 1 digit: max sum = 1 × 59,049 = 59,049
#          min number = 1
#          59,049 > 1 -  Possible
#
# 2 digits: max sum = 2 × 59,049 = 118,098
#           min number = 10
#           118,098 > 10 -  Possible
#
# 3 digits: max sum = 3 × 59,049 = 177,147
#           min number = 100
#           177,147 > 100 -  Possible
#
# 4 digits: max sum = 4 × 59,049 = 236,196
#           min number = 1,000
#           236,196 > 1,000 -  Possible
#
# 5 digits: max sum = 5 × 59,049 = 295,245
#           min number = 10,000
#           295,245 > 10,000 - Possible
#
# 6 digits: max sum = 6 × 59,049 = 354,294
#           min number = 100,000
#           354,294 > 100,000 - Possible
#
# 7 digits: max sum = 7 × 59,049 = 413,343
#           min number = 1,000,000
#           413,343 < 1,000,000 - Impossible

total = 0
upper_bound = 6 * (9**5)


def is_sum(n):
    summation: int = 0
    n = str(n)
    for i in range(len(n)):
        summation += int(n[i]) ** 5
    if summation == int(n):
        return True
    else:
        return False


for num in range(2, upper_bound + 1):  # Start from 2 since 1 is not a sum
    if is_sum(num):
        print(f"Found: {num}")
        total += num
print(total)
