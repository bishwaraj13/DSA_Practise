# https://leetcode.com/problems/remove-outermost-parentheses/
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        counter = 0
        result_str = ""

        for ch in s:
            if ch == '(':
                counter += 1
                if counter > 1:
                    result_str += ch
            else:
                counter -= 1
                if counter > 0:
                    result_str += ch

        return result_str
