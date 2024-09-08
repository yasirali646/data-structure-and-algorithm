"""
    Problem: Find the Only Non-Repeating Element
    In an array where every element appears twice except for one element, find that single non-repeating element using bitwise XOR.

"""

class Solution:
    def find_single(nums):
        result = 0
        for num in nums:
            result ^= num
        return result

    
print(Solution.find_single([1, 2, 2, 3, 1]))
