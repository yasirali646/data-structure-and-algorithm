"""
    Remove Duplicates from Sorted Array
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.

"""

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        l = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[l]:
                l += 1
                nums[l] = nums[i]
        return l + 1
        

nums = [1, 1, 2]
print(Solution().removeDuplicates(nums))