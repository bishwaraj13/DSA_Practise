# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge cases
        if not needle:
            return 0
        if not haystack or len(needle) > len(haystack):
            return -1
        
        # Brute force approach: check every possible starting position
        for i in range(len(haystack) - len(needle) + 1):
            # Check if substring starting at position i matches needle
            if haystack[i:i+len(needle)] == needle:
                return i
        
        # If no match found
        return -1