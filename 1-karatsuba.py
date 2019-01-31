#!/usr/bin/env python

import math


def karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y
    else:
        if x is not 0 and y is not 0:
            # find the max of x or y
            m = int(max((math.log10(x)) + 1, (math.log10(y)) + 1))
        elif x is not 0:
            m = int(math.log10(x))
        else:
            m = int(math.log10(y))
        m2 = math.ceil(m / 2)

        # convert multiplicands to strings and then split them in half
        # these will result in a ValueError if the str is ''
        a = int(str(x)[0:-m2]) if str(x)[0:-m2] is not '' else 0
        b = int(str(x)[-m2:m]) if str(x)[-m2:m] is not '' else 0
        c = int(str(y)[0:-m2]) if str(y)[0:-m2] is not '' else 0
        d = int(str(y)[-m2:m]) if str(y)[-m2:m] is not '' else 0

        step1 = karatsuba(a, c)
        step2 = karatsuba(b, d)
        step3 = karatsuba((a + b), (c + d))
        step4 = step3 - step2 - step1
        step5 = step1*10**(2*m2) + step2 + step4*10**m2
        return step5


print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                2718281828459045235360287471352662497757247093699959574966967627))
