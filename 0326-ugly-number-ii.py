#!/usr/bin/env python3

def ugly_number(n):

    if n > 2**31-1 or n < -2**31 or n == 0 or n == 1 or n == 2 or n == -1 or n == -2: return False

    divisor = 2
    factors = []
    while divisor * divisor <= n:
        if n % divisor:
            divisor += 1
        else:
            n //= divisor
            factors.append(divisor)
    if n > 1:
        factors.append(n)
    return set(factors) | set([2, 3, 5]) == set([2, 3, 5])


def ugly_number_ii(k):

    x = [0, 1]
    count = 1
    while len(x) < k:
        count += 1
        if ugly_number(count):
            x.append(count)
    return x[-1]
            

ugly_number_ii(5) == 5, 'Fail'
ugly_number_ii(10) == 12, 'Fail'
ugly_number_ii(13) == 18, 'Fail'
ugly_number_ii(52) == 256, 'Fail'
