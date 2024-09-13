"""
    Problem: Set or clear a specific bit
    Set (make 1) or clear (make 0) a specific bit at a given position.
"""

class Solution:
    def set_bit(num, k): 
        return num | (1 << k)
    
    def clear_bit(num, k): 
        return num & ~(1 << k)
    


result1 = Solution.set_bit(5, 1)
print(result1)

result2 = Solution.clear_bit(6, 1)
print(result2)