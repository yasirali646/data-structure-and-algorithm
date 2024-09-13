"""
    Problem: Find the ith bit in a number
    Find whether the ith bit is 1 or 0.   
"""

class Solution:
    def get_ith_bit(n, i):
        return (n >> i) & 1
    

print(Solution.get_ith_bit(5, 1))