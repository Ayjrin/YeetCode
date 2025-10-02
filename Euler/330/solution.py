# Problem 330
# ===========
#
# An infinite sequence of real numbers a(n) is defined for all integers n as
# follows:
#
# [Image: 330_formula.gif]
#
# For example,
#
#         1     1     1
# a(0) = --- + --- + --- + ... = e - 1
#         1!    2!    3!
#
#        e − 1    1     1
# a(1) = ----- + --- + --- + ... = 2e - 3
#          1!     2!    3!
#
#        2e − 3   e − 1    1          7
# a(2) = ------ + ----- + --- + ... = - e - 6
#          1!       2!     3!         2
#
# with e = 2.7182818... being Euler's constant.
#
# It can be shown that a(n) is of the form:
#
# A(n) e + B(n)
# -------------
#       n!
#
# for integers A(n) and B(n).
#
# For example:
#
#         328161643e − 652694486
# a(10) = ----------------------
#                   10!
#
# Find A(10^9) + B(10^9) and give your answer mod 77 777 777.

