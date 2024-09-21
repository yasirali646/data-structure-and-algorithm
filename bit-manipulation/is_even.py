"""
    Problem: Check if a Number is Even or Odd
    Using only bitwise operators, write a function that checks if a number is even or odd.
"""


class Solution:
    def is_even(n):
        return not (n & 1)
    
    
s = Solution
print(s.is_even(10))