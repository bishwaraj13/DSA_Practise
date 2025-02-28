# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
from typing import *

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def possible(day, m, k):
            count = 0
            numberOfBouquet = 0

            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    count += 1
                else:
                    numberOfBouquet += (count // k)
                    count = 0

            numberOfBouquet += (count / k)
            
            if numberOfBouquet >= m:
                return True
            
            return False

        if len(bloomDay) < m * k:
            return -1

        low = min(bloomDay)
        high = max(bloomDay)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if possible(mid, m, k):
                high = mid - 1
            else:
                low = mid + 1

        return low