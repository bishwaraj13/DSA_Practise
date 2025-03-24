# https://leetcode.com/problems/shortest-palindrome/description/
# this is brute-force approach
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Edge cases
        if not s:
            return ""
        
        # Function to check if a string is palindrome
        def is_palindrome(string, start, end):
            while start < end:
                if string[start] != string[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        # Find the longest palindromic prefix
        n = len(s)
        right = n - 1
        
        # Start from the end and move left until we find a palindromic prefix
        while right >= 0:
            if is_palindrome(s, 0, right):
                break
            right -= 1
        
        # If the entire string is a palindrome, return it
        if right == n - 1:
            return s
        
        # Get the remaining part of the string, reverse it, and add to the beginning
        remaining = s[right + 1:]
        reversed_remaining = remaining[::-1]
        
        return reversed_remaining + s