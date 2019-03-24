#!/usr/bin/env python3

def roman_to_integer(roman):
    _roman_ = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    _integer_ = 0
    for i in range(len(roman)):
        if i > 0 and _roman_[roman[i]] > _roman_[roman[i - 1]]:
            _integer_ += _roman_[roman[i]] - 2 * _roman_[roman[i - 1]]
        else:
            _integer_ += _roman_[roman[i]]
    return _integer_

assert roman_to_integer("MMMCCCXXXIII") == 3333, 'Fail'
assert roman_to_integer("MCDXXXVII") == 1437, 'Fail'
assert roman_to_integer("I") == 1, 'Fail'
