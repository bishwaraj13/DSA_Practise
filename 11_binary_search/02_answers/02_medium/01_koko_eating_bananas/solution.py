# https://leetcode.com/problems/koko-eating-bananas/
from typing import *
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_taken(speed):
            total_time = 0
            for bananas in piles:
                total_time += math.ceil(float(bananas)/speed)

            return total_time
        
        # minimum speed koko may take to eat would be 1
        # maximum speed koko may take to eat would be max(piles)
        # So, its a binary search of k from 1 to max(piles)

        low = 1
        high = max(piles)
        result = high

        while low <= high:
            mid = (low + high) // 2

            time_to_eat = time_taken(mid)

            # koko took less time to eat
            # => his speed is fast, but koko definitely finished his bananas
            # => we can try to decrease his speed, and look for more solutions till we don't find one
            if time_to_eat <= h:
                high = mid - 1
                result = mid
            # koko took more time to eat
            # his speed is slow
            # => we need to increase his speed
            elif time_to_eat > h:
                low = mid + 1

        return result
