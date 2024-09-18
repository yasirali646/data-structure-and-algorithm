"""
    Valid Palindrome
    
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.
"""

import re

class Solution:
    def isPalindrome(self, s):
        if len(s.strip()) == 0:
            return True
        
        s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        l,r = 0,len(s)-1

        while r > l:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


result = Solution().isPalindrome("A man, a plan, a canal: Panama")

print(result)