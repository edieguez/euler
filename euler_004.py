#! /usr/bin/env python3
'''
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

palindrome = 0
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        n = i * j
        if n > palindrome:
            palindrome = n if str(n) == str(n)[::-1] else palindrome

print(palindrome)
