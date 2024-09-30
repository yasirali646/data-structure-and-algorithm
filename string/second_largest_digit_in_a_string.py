"""
    Second Largest Digit in a String
    
    Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

    An alphanumeric string is a string consisting of lowercase English letters and digits.

"""

class Solution:
    def secondHighest(self, s: str) -> int:
        digits = {int(c) for c in s if c.isdigit()}
    
        sorted_digits = sorted(digits, reverse=True)    
        
        return sorted_digits[1] if len(sorted_digits) > 1 else -1
