#!/usr/bin/env python

import math


def karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y
    # if x == 0 or y == 0:
    #     return 0
    else:
        if x is not 0 and y is not 0:
            # find the max of x or y
            m = int(max((math.log10(x)) + 1, (math.log10(y)) + 1))
        elif x is not 0:
            m = int(math.log10(x))
        else:
            m = int(math.log10(y))
        # m = int(max(len(str(x)), len(str(y))))
        # print(int(math.log10(x))+1)
        m2 = math.ceil(m / 2)

        # convert multiplicands to strings and then split them in half
        # these will result in a ValueError if the str is ''
        a = int(str(x)[0:-m2]) if str(x)[0:-m2] is not '' else 0
        b = int(str(x)[-m2:m]) if str(x)[-m2:m] is not '' else 0
        c = int(str(y)[0:-m2]) if str(y)[0:-m2] is not '' else 0
        d = int(str(y)[-m2:m]) if str(y)[-m2:m] is not '' else 0

        # a = math.floor(x / 10 ** m2)
        # b = x % 10 ** m2
        # c = math.floor(y / 10 ** m2)
        # d = y % 10 ** m2
        # if len(str(b)) != len(str(d)):
        #     print(False)

        step1 = karatsuba(a, c)
        step2 = karatsuba(b, d)
        # print('b: {b}, d: {d}'.format(b=b, d=d))
        step3 = karatsuba((a + b), (c + d))
        step4 = step3 - step2 - step1
        # print(step1*10**2*m2)
        # print(step2)
        # print(step4*10**m2)
        step5 = (step1*10**(2*m2)) + (step2) + (step4*10**(m2))
        return(step5)

# print(karatsuba(11567, 554433))

print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 
2718281828459045235360287471352662497757247093699959574966967627))




# 1) a * c: GOOD
# print(karatsuba(31415926535897932384626433832795, 27182818284590452353602874713526))
#            853973422267356706546355086954637031247909995660108279808885170
#            853973422267356706546355086954637031247909995660108279808885170

# 2) b * d: BAD
# print(karatsuba(2884197169399375105820974944592, 62497757247093699959574966967627))
#                                                                            180255854545876960157244878324300131223124341791952806582723184
#                                                                            180255854545876931315273184330549073013374895871952806582723184
#                                                                            1802558545458769958479645294604031721651638412861952806582723184
# 3) b * d of (2): GOOD
# print(karatsuba(5105820974944592, 9959574966967627))
#                                                                                                           50851806767876401952806582723184
#                                                                                                           50851806767876401952806582723184
# 4) a * c of (2): GOOD
# print(karatsuba(2884197169399375, 6249775724709369))
#                                                                            18025585454587689597632165244375
#                                                                            18025585454587689597632165244375
# 5) (a + b) * (c + d) of (2): GOOD
# print(karatsuba((2884197169399375+5105820974944592), (6249775724709369+6249775724709369)))
#                99871642877016648086984487053646
#                99871642877016648086984487053646
# problem must be in step 5 then


# mine:      8539734222673566957498846900491595793628487889746454950813687461572372213054499114931277629325900131223124341791952806582723184
#            8539734222741967044636107894353299989106225851949199680340544763362460622088376700057603497916432537443153023022389712581823184
#            8539734222741967153090090158638514132503608418533065336905844490421604760710273353716300940806781479233403577102389712581823184
#            8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
# mathisfun: 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184


# def karatsuba(x, y):
#     """Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
#     if x < 10 and y < 10:
#         return x * y
#     
#     #if len(str(x)) == 1 or len(str(y)) == 1:
#     #    return x * y
#     
#     else:
#         n = max(int(math.log10(x)), int(math.log10(y)))
#         # n = max(len(str(x)), len(str(y)))
#         nby2 = n / 2
# 
#         a = x / 10 ** (nby2)
#         b = x % 10 ** (nby2)
#         c = y / 10 ** (nby2)
#         d = y % 10 ** (nby2)
# 
#         ac = karatsuba(a, c)
#         bd = karatsuba(b, d)
#         ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
# 
#         # this little trick, writing n as 2*nby2 takes care of both even and odd n
#         prod = ac * 10 ** (2 * nby2) + (ad_plus_bc * 10 ** nby2) + bd
# 
#     return prod