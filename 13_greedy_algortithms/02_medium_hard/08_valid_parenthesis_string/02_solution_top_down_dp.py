# https://leetcode.com/problems/valid-parenthesis-string/description/
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        # this is how you initialise 2d array without list comprehension
        # dp_cache = []
        # for i in range(n):
        #     row = []
        #     for j in range(n):
        #         row.append(-1)
        #     dp_cache.append(row)
        dp_cache = [[-1 for j in range(n)] for i in range(n)]

        def isValid(index, counter):
            if counter < 0:
                return False

            if index == len(s):
                if counter == 0:
                    return True
                return False

            if dp_cache[index][counter] is not -1:
                return dp_cache[index][counter]

            if s[index] == '(':
                result = isValid(index+1, counter+1)
            elif s[index] == ')':
                result = isValid(index+1, counter-1)
            else:
                result = (
                    isValid(index+1, counter+1) or 
                    isValid(index+1, counter-1) or
                    isValid(index+1, counter)
                )

            dp_cache[index][counter] = result
            return result

        return isValid(0, 0)