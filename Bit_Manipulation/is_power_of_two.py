"""
    Problem: Power of Two
    Write a function that checks if a given integer is a power of 2 using bitwise operators.
"""

class Solution:
    def is_power_of_two(n):
        return n > 0 and (n & (n - 1)) == 0
    

s = Solution
print(s.is_power_of_two(8))
