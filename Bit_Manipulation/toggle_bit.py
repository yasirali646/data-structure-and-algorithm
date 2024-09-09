"""
        Problem: Toggle a specific bit
        Toggle (invert) a specific bit at a given position.
"""

class Solution:

    def toggle_bit(n, k):
        return n ^ (1 << k)

result = Solution.toggle_bit(5, 1)
print(result)