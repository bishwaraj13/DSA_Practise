# https://leetcode.com/problems/sliding-window-maximum/
from collections import deque
from typing import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        answer = []

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            
            stack.append(i)

            # remove element if we exceeded the window size
            if stack[0] <= i-k:
                stack.popleft()

            if i - (k - 1) >= 0:
                # cause its decreasing stack, the bottom element is highest
                answer.append(nums[stack[0]])

        return answer