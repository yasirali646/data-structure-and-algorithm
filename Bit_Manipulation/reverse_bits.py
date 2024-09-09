"""
        Problem: Reverse the bits of a number
        Reverse the bits in the binary representation of a number.
"""

class Solution:
    def reverse_bits(n):
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

result = Solution.reverse_bits(2)
print(result)