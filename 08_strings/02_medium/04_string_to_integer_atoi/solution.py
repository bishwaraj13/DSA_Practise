# https://leetcode.com/problems/string-to-integer-atoi/
# this has too many edge cases - found it difficult to get it right in one go
class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        started = False

        for ch in s:
            if not started and ch == '-':
                sign = -1
                started = True
                continue

            if not started and ch == '+':
                started = True
                continue

            # get digit
            digit = ord(ch) - ord('0')

            if ord('0') <= ord(ch) <= ord('9'):
                # its a valid digit
                started = True
                result = result * 10 + digit
            elif ch == ' ' and not started:
                # wait to start
                continue  
            else:
                # we have reached the end of the number
                break
           
        result *= sign
        # Clamp the result to the 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        result = max(min(result, INT_MAX), INT_MIN)

        return result
        