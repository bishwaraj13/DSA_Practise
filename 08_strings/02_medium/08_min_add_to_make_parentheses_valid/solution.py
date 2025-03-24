# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        result = 0

        for ch in s:
            if ch == "(":
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    result += 1

        return open + result