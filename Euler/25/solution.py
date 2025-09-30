# The Fibonacci sequence is defined by the recurrence relation:

#   F[n] = F[n−1] + F[n−2], where F[1] = 1 and F[2] = 1.

# Hence the first 12 terms will be:

#   F[1] = 1
#   F[2] = 1
#   F[3] = 2
#   F[4] = 3
#   F[5] = 5
#   F[6] = 8
#   F[7] = 13
#   F[8] = 21
#   F[9] = 34
#   F[10] = 55
#   F[11] = 89
#   F[12] = 144

# The 12th term, F[12], is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
def fibonacci(n: int):
    a = 0
    b = 1

    if n < 0:
        print("n<0")
        return None, None
    elif n == 0:
        return 0, 0
    elif n == 1:
        return b, n
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b, n


def find_thousand_digit_number(n: int):
    length = 0
    fibby = 0
    index = 0
    while length < 1_000:
        fibby, index = fibonacci(n)
        n += 1
        length = len(str(fibby))
    print(fibby)
    print(index)


find_thousand_digit_number(1)
