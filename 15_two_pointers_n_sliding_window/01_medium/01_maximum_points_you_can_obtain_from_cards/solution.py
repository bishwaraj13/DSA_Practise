# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# This is case of constant window, but has a slight twist
from typing import *

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        l = k-1
        r = n-1

        total = sum(cardPoints[0:l+1])
        max_sum = total

        while l >= 0:
            total -= cardPoints[l]
            l -= 1
            total += cardPoints[r]
            r -= 1
            max_sum = max(total, max_sum)

        return max_sum
        