#!/usr/bin/env python3

def to_lower_case(string):
    return ''.join([chr(ord(char) + 32) if ord(char) >= ord('A') and ord(char) <= ord('Z') else char for char in string])

assert to_lower_case("QWERTYsa~!@#$%^&*()_1234567890-.sdjiwdksUIOPASDFGHJKL") == "QWERTYsa~!@#$%^&*()_1234567890-.sdjiwdksUIOPASDFGHJKL".lower(), 'Fail'
