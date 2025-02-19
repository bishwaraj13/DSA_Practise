# https://leetcode.com/problems/fruit-into-baskets/description/
from typing import *

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0

        max_len = 0
        fruits_count = {}

        while r < len(fruits):
            fruits_count[fruits[r]] = fruits_count.get(fruits[r], 0) + 1

            while len(fruits_count) > 2:
                fruits_count[fruits[l]] -= 1

                if fruits_count[fruits[l]] == 0:
                    del fruits_count[fruits[l]]

                l += 1

            max_len = max(max_len, r-l+1)
            r += 1

        return max_len  
        