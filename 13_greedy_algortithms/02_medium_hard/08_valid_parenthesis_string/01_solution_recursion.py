# https://leetcode.com/problems/valid-parenthesis-string/description/
class Solution:
    def checkValidString(self, s: str) -> bool:
        def isValid(index, counter):
            if counter < 0:
                return False

            if index == len(s):
                if counter == 0:
                    return True
                return False

            if s[index] == '(':
                return isValid(index+1, counter+1)
            elif s[index] == ')':
                return isValid(index+1, counter-1)
            else:
                return (
                    isValid(index+1, counter+1) or 
                    isValid(index+1, counter-1) or
                    isValid(index+1, counter)
                )

        return isValid(0, 0)
