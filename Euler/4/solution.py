# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


# maybe this could be improved by not making an array, but walking backwards from 999 rather than getting all the answers up until 999 and then compare the new palindrome to the incumbant largest and stop when both products are below the lowest product that found the incumabent palindrome
# but who has time for that. good enough is great for now.
def simple():
    palindromes = []

    for i in range(100, 999):
        for j in range(100, 999):
            num_to_check = i * j
            if str(num_to_check) == str(num_to_check)[::-1]:
                palindromes.append(num_to_check)

    print(max(palindromes))

simple()








# THOUGHT PROCESS
#
# can be the same in both direction. I need to take the number and convert it to an array of chars and then invert the compile
# actually, i think it would be better, to reduce space complexity, to have a single array and then start at the middle and work ourselves outwards with two readers, then we can compare each one that the reader sees and then compare. when it fails a check we return as a fail. if one gets to the end before another, it returns as a fail. only if they get to position 0 and they still agree is it a success

#This was a bunch of nonsense. After trying this for like 45 mins, I just thought there has to be a python way to reverse a string... obv. as soon as i found that, this became a dumb simple problem.
# def make_list_of_numbers(num):
#     chars = list(str(num))

#     print(chars)
#     return chars

# def check_list_for_palindrome(chars) -> bool:
#     lower, upper = (len(chars)//2)-1, (len(chars)//2)
#     while lower > 0:
#         print("upper " + str(upper))
#         print("lower " + str(lower))

#         if chars[lower] != chars[upper]:
#             print("false")
#             print(chars[lower])
#             print(chars[upper])

#             return False

#         lower -= 1
#         upper += 1
#     print("true")
#     return True


# def solve():

#     beeg_palindrome = False
#     prod1 = 999
#     prod2 = 999

#     while prod1 > 100:
#         while prod2 > 100:
#             while not beeg_palindrome:
#                 num_to_check = prod1 * prod2
#                 if check_list_for_palindrome(make_list_of_numbers(num_to_check)):
#                     beeg_palindrome = True

#             prod2 -= 1
#         prod2 = 999
#         prod1 -= 1
