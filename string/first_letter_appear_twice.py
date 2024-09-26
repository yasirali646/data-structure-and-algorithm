"""
    First Letter to Appear Twice

    Given a string s consisting of lowercase English letters, return the first letter to appear twice.

    A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
    s will contain at least one letter that appears twice.
"""

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        stack = []
        for c in s:
            if c in stack:
                return c
            else:
                stack.append(c)