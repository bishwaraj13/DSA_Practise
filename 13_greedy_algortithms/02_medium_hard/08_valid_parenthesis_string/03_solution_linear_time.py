# https://leetcode.com/problems/valid-parenthesis-string/description/
class Solution:
    def checkValidString(self, s: str) -> bool:
        # we initially assume no string,
        # meaning count is 0
        # In this case, we consider range
        mini = 0
        maxi = 0

        for i in range(len(s)):
            if s[i] == '(':
                mini += 1
                maxi += 1
            elif s[i] == ')':
                mini -= 1
                maxi -= 1
            else:
                mini -= 1
                maxi += 1

            if mini < 0:
                mini = 0

            if maxi < 0:
                return False
        
        return mini == 0