# https://leetcode.com/problems/palindrome-partitioning/
from typing import *

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        
        def isPalindrome(substring):
            return substring == substring[::-1]
        
        def backtrack(st_indx):
            # Base case: if we've reached the end of the string
            if st_indx == len(s):
                res.append(path.copy())
                return
            
            # Try all possible ending positions for current partition
            for end_indx in range(st_indx, len(s)):
                # Check if substring s[st_indx:end_indx+1] is palindrome
                if isPalindrome(s[st_indx:end_indx+1]):
                    # Add current palindrome to path
                    path.append(s[st_indx:end_indx+1])
                    # Recur for remaining string
                    backtrack(end_indx + 1)
                    # Backtrack (remove the current palindrome from path)
                    path.pop()
        
        backtrack(0)
        return res