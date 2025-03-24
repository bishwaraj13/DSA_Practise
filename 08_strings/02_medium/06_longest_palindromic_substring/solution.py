# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        end = 0
        max_length = 1
        
        # Helper function to expand around center
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of palindrome
            return right - left - 1, left + 1, right - 1
        
        # Check each position as potential center
        for i in range(len(s)):
            # Odd length palindrome (single character center)
            len1, start1, end1 = expand_around_center(i, i)
            
            # Even length palindrome (two character center)
            len2, start2, end2 = expand_around_center(i, i+1)
            
            # Update if we found a longer palindrome
            if len1 > max_length:
                max_length = len1
                start = start1
                end = end1
            
            if len2 > max_length:
                max_length = len2
                start = start2
                end = end2
        
        return s[start:end+1]