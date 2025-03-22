# https://leetcode.com/problems/next-greater-element-ii/
from typing import *

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # initialize nextGreater array, this array holds the output
        # initialize all the elements as -1 (invalid value)
        next_greater = [-1] * n
        stack = []
        
        # Run the loop twice to simulate circular array
        for j in range(2):
            # iterate through all the elements of the array
            for i in range(n):
                # While stack is not empty and current element is greater than the element at stack top index
                while stack and nums[stack[-1]] < nums[i]:
                    # Pop the top element and update its next greater element
                    stack_top = stack.pop()
                    next_greater[stack_top] = nums[i]
                    
                stack.append(i)
                
        return next_greater