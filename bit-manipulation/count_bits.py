"""
    Problem 1: Count Set Bits
    Write a function that counts the number of 1s in the binary representation of a given integer.

"""

class Solution:
    def count_bits(n):
        c = 0
        while n:
            n &= (n - 1)
            c += 1
        return c;


s = Solution
print(s.count_bits(10))