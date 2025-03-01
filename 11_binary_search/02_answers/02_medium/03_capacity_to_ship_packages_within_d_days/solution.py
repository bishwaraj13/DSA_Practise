# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
from typing import *

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def findDays(capacity):
            days = 1
            load = 0

            for i in range(len(weights)):
                if weights[i] + load > capacity:
                    days += 1
                    load = weights[i]
                else:
                    load += weights[i]

            return days

        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2
            numberOfDays = findDays(mid)

            if numberOfDays <= days:
                high = mid - 1
            else: 
                low = mid + 1

        return low