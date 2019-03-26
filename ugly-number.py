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


assert ugly_number(6) is True , 'fall'
assert ugly_number(11) is False , 'fall'
assert ugly_number(14) is False , 'fall'
assert ugly_number(2**31) is False, 'fall'
assert ugly_number(-2**31-1) is False , 'fall'
assert ugly_number(30000000000) is False , 'fall'
assert ugly_number(1) is False, 'fall'
assert ugly_number(0) is False, 'fall'
assert ugly_number(-2) is False, 'fall'
