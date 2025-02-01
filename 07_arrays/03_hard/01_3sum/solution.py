# https://leetcode.com/problems/3sum/
from typing import List

# the following code is correct if there are no duplicates in the input array
# see below for better solution
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         triplets = []

#         for i in range(len(nums)-3):
#             pivot = nums[i]
#             hashmap = {}

#             for j in range(i+1, len(nums)):
#                 current_elem = nums[j]
#                 x = -pivot-current_elem

#                 if x in hashmap:
#                     triplets.append([pivot, current_elem, x])

#                 hashmap[current_elem] = j

#         return triplets

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array - O(nlogn)
        nums = sorted(nums)
        triplets = []

        for i in range(len(nums)-2):
            # skip duplicates
            if i != 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            left = i+1
            right = len(nums) - 1

            while left < right:
                if (nums[left] + nums[right]) == target:
                    triplets.append([-target, nums[left], nums[right]])

                    # skip duplicates for left
                    while left < right and nums[left] == nums[left+1]:
                        left += 1

                    left += 1

                    # skip duplicates for right
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    right -= 1

                elif (nums[left] + nums[right]) < target:
                    left += 1
                else:
                    right -= 1

        return triplets
    