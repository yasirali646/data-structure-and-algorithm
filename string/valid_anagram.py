"""
    Valid Anagram
    
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str): 
        
        if len(s) != len(t):
            return False
        
        return Counter(s) == Counter(t)
