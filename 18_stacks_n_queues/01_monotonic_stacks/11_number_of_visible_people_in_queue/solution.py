# https://leetcode.com/problems/number-of-visible-people-in-a-queue/
from typing import *

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(heights)
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                # next greater section
                stack_top = stack.pop()
                # process
                answer[stack_top] += 1
            
            if stack:
                # previous greater section
                # process
                answer[stack[-1]] += 1
            
            stack.append(i)
        
        return answer
