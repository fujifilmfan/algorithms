#!/usr/bin/env python

import math


"""
In this programming assignment you will implement one or more of the integer multiplication algorithms described in
lecture.

To get the most out of this assignment, your program should restrict itself to multiplying only pairs of
single-digit numbers. You can implement the grade-school algorithm if you want, but to get the most out of the
assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm.

So: what's the product of the following two 64-digit numbers?
3141592653589793238462643383279502884197169399375105820974944592
2718281828459045235360287471352662497757247093699959574966967627
"""


def karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y
    else:
        if x is not 0 and y is not 0:
            # Find the max of x or y
            m = int(max((math.log10(x)) + 1, (math.log10(y)) + 1))
        elif x is not 0:
            m = int(math.log10(x))
        else:
            m = int(math.log10(y))
        m2 = math.ceil(m / 2)

        # Convert multiplicands to strings and then split them in half
        # These will result in a ValueError if the str is ''
        a = int(str(x)[0:-m2]) if str(x)[0:-m2] is not '' else 0
        b = int(str(x)[-m2:m]) if str(x)[-m2:m] is not '' else 0
        c = int(str(y)[0:-m2]) if str(y)[0:-m2] is not '' else 0
        d = int(str(y)[-m2:m]) if str(y)[-m2:m] is not '' else 0

        # These are the steps for Karatsuba multiplication
        step1 = karatsuba(a, c)
        step2 = karatsuba(b, d)
        step3 = karatsuba((a + b), (c + d))
        step4 = step3 - step2 - step1
        step5 = step1*10**(2*m2) + step2 + step4*10**m2
        return step5


print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                2718281828459045235360287471352662497757247093699959574966967627))
