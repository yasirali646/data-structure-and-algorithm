"""
    Remove Element

    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

    Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    Return k.
"""

# Solution: 1
class Solution1:
    def removeElement(nums, val):
        
        if val not in nums:
            return len(nums)

        n = len(nums)

        l,r = 0, n - 1

        while l <= r:
            if nums[l] == val and nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -+1
            if nums[l] != val:
                l += 1
            if nums[r] == val:
                r -= 1
        return r + 1
            
            
            
            
# Solution: 2
class Solution2:
    def removeElement(nums, val):
        e = 0
        
        for num in nums:
            if num != val:
                nums[e] = num
                e += 1
        return e
    

print(Solution1.removeElement([0,1,2,2,3,0,4,2], 2))                 
print(Solution2.removeElement([0,1,2,2,3,0,4,2], 2))                 
