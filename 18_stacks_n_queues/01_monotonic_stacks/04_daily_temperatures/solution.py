# https://leetcode.com/problems/daily-temperatures/
from typing import *

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize an empty stack
        stack = []

        # initialize nextGreater array, this array holds the output
        # initialize all them elements as 0 (invalid value)
        next_greater = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                stack_top = stack.pop()
                # i - stackTop is the number of days to wait
                next_greater[stack_top] = i - stack_top

            stack.append(i)

        return next_greater