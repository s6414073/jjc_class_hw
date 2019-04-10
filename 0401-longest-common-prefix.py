#!/usr/bin/env python3

def longest_common_prefix(strs):

   if not strs:
       return ''
   for i, chars in enumerate(zip(*strs)):
       if len(set(chars)) > 1:
           return strs[0][:i]
   return min(strs)

assert longest_common_prefix(["flower","flow","flight"]) == "fl", 'Fail'
assert longest_common_prefix(["dog","racecar","car"]) == "", 'Fail'

