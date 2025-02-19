# https://leetcode.com/problems/fruit-into-baskets/description/
# This is an improvement over prev solution
# It removed inner loop, and use if condition
# This means we dont go below maxlen, because there is no need..
# we just keep looking for more maxlen, not less than what we already achieved
from typing import *

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0

        max_len = 0
        fruits_count = {}

        while r < len(fruits):
            fruits_count[fruits[r]] = fruits_count.get(fruits[r], 0) + 1

            if len(fruits_count) > 2:
                fruits_count[fruits[l]] -= 1

                if fruits_count[fruits[l]] == 0:
                    del fruits_count[fruits[l]]

                l += 1

            if len(fruits_count) <= 2:
                max_len = max(max_len, r-l+1)
            r += 1

        return max_len  
        