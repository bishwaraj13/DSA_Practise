# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = ''.join(ch.lower() for ch in s if ch.isalnum())
        return self.isPalindromeRecursive(cleanStr, 0, len(cleanStr)-1)

    def isPalindromeRecursive(self, s: str, left: int, right: int):
        if left >= right:
            return True

        if s[left] != s[right]:
            return False

        return self.isPalindromeRecursive(s, left+1, right-1)