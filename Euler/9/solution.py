# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

# def sove() -> int:
#     for a in range(500):
#         for b in range(500):

#             csquared = a**2 + b**2
#             c = math.sqrt(csquared)
#             if a + b + c == 1000:
#                 prod = a*b*c
#                 print(a, b, c)
#                 return int(prod)

#             elif a + b + c > 1000:
#                 return int(0)
#     return int(0)

# print(sove())

for a in range(1, 500):
    b = 1000 * (500-a) / (1000-a)
    c = math.sqrt(a**2 + b**2)
    if int(math.floor(c)) == c and 0 < a < b < c:
        print(a, b, c)
        print(int(a*b*c))
