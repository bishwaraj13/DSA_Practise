# https://leetcode.com/problems/rotate-string/
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        extended_s = s + s

        for i in range(len(s)):
            if goal == extended_s[i:i+len(s)]:
                return True

        return False