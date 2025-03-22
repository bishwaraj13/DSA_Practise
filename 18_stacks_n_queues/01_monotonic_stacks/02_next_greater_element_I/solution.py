# https://leetcode.com/problems/next-greater-element-i/description/
from typing import *

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Map to store indices of nums2 elements for quick lookup
        nums2_indices = {num: i for i, num in enumerate(nums2)}
        
        # Initialize result array with -1 (default when no greater element exists)
        next_greater = [-1] * len(nums2)
        
        # Initialize an empty stack to store indices
        stack = []
        
        # Process nums2 to find next greater elements
        for i in range(len(nums2)):
            # While stack is not empty and current element is greater than the element at stack top index
            while stack and nums2[stack[-1]] < nums2[i]:
                # Pop the top index from stack
                stack_top = stack.pop()
                
                # Set the next greater element for the popped index
                next_greater[stack_top] = nums2[i]
            
            # Push the current index onto the stack
            stack.append(i)
        
        # Build result array for nums1
        result = []
        for num in nums1:
            idx = nums2_indices[num]  # Get the index of this number in nums2
            result.append(next_greater[idx])  # Use the precomputed next greater element
        
        return result