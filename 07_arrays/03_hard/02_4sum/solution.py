# https://leetcode.com/problems/4sum/
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        quadruplets = []

        for h in range(0, len(nums)-3):
            # skip the duplicates
            if h > 0 and nums[h] == nums[h-1]:
                continue

            pivot_1 = target - nums[h]

            # 3 sum problems from here
            for i in range(h+1, len(nums)-2):
                # skip the duplicates
                if i > h+1 and nums[i] == nums[i-1]:
                    continue

                pivot_2 = pivot_1 - nums[i]

                # 2 sum problems
                left = i+1
                right = len(nums) - 1

                while left < right:
                    if (nums[left]+nums[right] == pivot_2):
                        quadruplets.append([nums[h], nums[i], nums[left], nums[right]])

                        # skip duplicates for left
                        while left < right and nums[left] == nums[left+1]:
                            left += 1

                        left += 1

                        # skip duplicates for right
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1

                        right -= 1

                    elif (nums[left] + nums[right] < pivot_2):
                        left += 1
                    else:
                        right -= 1

        return quadruplets
            