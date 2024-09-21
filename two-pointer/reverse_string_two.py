"""
    Reverse String II
    
    Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

    If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.
"""

class Solution:
    def reverseStr(self, s, k):

        s = list(s)
        n = len(s)
        left = 0
        right = k - 1 if n > k else n - 1

        def swap(i, j):
            while i <= j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1                

        while left < n and left < right:
            if n > right or k > n:
                swap(left, right)
            left += k*2
            right = left + k - 1 if n - left > k else n - 1
        return ''.join(s)


result = Solution().reverseStr("abcdefg", 2)
print(result)