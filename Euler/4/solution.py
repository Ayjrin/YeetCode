# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# THOUGHT PROCESS
#
# can be the same in both direction. I need to take the number and convert it to an array of chars and then invert the compile
# actually, i think it would be better, to reduce space complexity, to have a single array and then start at the middle and work ourselves outwards with two readers, then we can compare each one that the reader sees and then compare. when it fails a check we return as a fail. if one gets to the end before another, it returns as a fail. only if they get to position 0 and they still agree is it a success


def make_list_of_numbers():
    num = 9009
    chars = list(str(num))

    print(chars)
    return chars

def check_list_for_palindrome(chars) -> bool:
    lower, upper = (len(chars)//2)-1, (len(chars)//2)
    while lower >= 1:
        print("upper " + str(upper))
        print("lower " + str(lower))

        if chars[lower] != chars[upper]:
            print("false")
            print(chars[lower])
            print(chars[upper])

            return False

        lower -= 1
        upper += 1
    print("true")
    return True

check_list_for_palindrome(make_list_of_numbers())
