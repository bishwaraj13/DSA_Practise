# https://leetcode.com/problems/largest-odd-number-in-string/description/
class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        
        # iterate from right to left
        for i in range(len(num)-1, -1, -1):
            ch = num[i]
            ch_num = int(num[i])

            if ch_num % 2 != 0:
                return num[0:i+1]

        return ""