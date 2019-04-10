#!/usr/bin/env python3

def climbing_stairs1(n):
    if n <= 2:
        return n
    else:
        return climbing_stairs1(n-1) + climbing_stairs1(n-2)

def climbing_stairs2(n): 
    num = [0, 1, 2]
    if n <= 2:
        return num[n]
    else:
        for i in range(3, n+1):
            num.append(num[i-1] + num[i-2])
        return num[n]


assert climbing_stairs1(1) == 1, 'Fail'
assert climbing_stairs1(2) == 2, 'Fail'
assert climbing_stairs1(3) == 3, 'Fail'
assert climbing_stairs1(4) == 5, 'Fail'
assert climbing_stairs1(5) == 8, 'Fail'
assert climbing_stairs1(6) == 13, 'Fail'
#assert climbing_stairs1(45) == 1836311903, 'Fail'

assert climbing_stairs2(1) == 1, 'Fail'
assert climbing_stairs2(2) == 2, 'Fail'
assert climbing_stairs2(3) == 3, 'Fail'
assert climbing_stairs2(4) == 5, 'Fail'
assert climbing_stairs2(5) == 8, 'Fail'
assert climbing_stairs2(6) == 13, 'Fail'
assert climbing_stairs2(45) == 1836311903, 'Fail'
