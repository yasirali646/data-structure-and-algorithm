"""
    Problem: Swap Two Numbers without Using a Temporary Variable
    Write a function that swaps two numbers using bitwise XOR without using a temporary variable.
"""

class Solution:
    def swap(a, b):
        a = a ^ b
        b = a ^ b
        a = a ^ b        
        return (a,b) 


s = Solution
print(s.swap(10, 12))
