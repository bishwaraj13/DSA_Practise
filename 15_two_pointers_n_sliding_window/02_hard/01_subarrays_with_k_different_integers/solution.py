# https://leetcode.com/problems/subarrays-with-k-different-integers/
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def count_subarrays_less_than_n_equal(q):
            if q <= 0:
                return 0
            l = 0
            r = 0
            hashmap = {}
            count = 0

            while r < len(nums):
                hashmap[nums[r]] = hashmap.get(nums[r], 0) + 1

                while len(hashmap) > q:
                    hashmap[nums[l]] -= 1

                    if hashmap[nums[l]] == 0:
                        del hashmap[nums[l]]

                    l += 1
  
                count += (r - l + 1)
                r += 1

            return count

        # count of subarrays with <= k distinct characters
        count1 = count_subarrays_less_than_n_equal(k)

        # count of subarrays with <= k-1 distinct characters
        count2 = count_subarrays_less_than_n_equal(k-1)

        return count1 - count2