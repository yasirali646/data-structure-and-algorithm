"""
    Problem: Turn Off Rightmost 1-bit
    Write a function that turns off the rightmost 1 bit in the binary representation of a number.

"""

class Solution:
    def turn_off_rightmost(n):
        return n & (n - 1)
        
        

result = Solution.turn_off_rightmost(9)
print(result)

