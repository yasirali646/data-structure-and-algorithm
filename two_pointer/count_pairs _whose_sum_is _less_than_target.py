"""
    Count Pairs Whose Sum is Less than Target
    
    Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

"""

class Solution:
    def countPairs(self, nums, target):
        n = len(nums) - 1
        l, r, c = 0, 1, 0

        while l < n:
            t = nums[l] + nums[r]

            if t < target:
                c += 1
                if r == n:
                    l += 1
                    r = l + 1
                else:
                    r += 1
            elif r == n:
                l += 1
                r = l + 1
            else:
                r += 1
        return c


result = Solution().countPairs([-1,1,2,3,1], 2)
print(result)