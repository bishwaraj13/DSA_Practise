# https://leetcode.com/problems/candy/
# Hard to come up with this
# But its easy when you draw and understand..
# in terms of increasing ratings, decreasing ratings and flat ratings
# solution explanation: https://www.youtube.com/watch?v=IIqVFvKE6RY
from typing import *

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        sum = 1
        i = 1

        while i < n:
            # flat surface
            if ratings[i] == ratings[i-1]:
                sum += 1
                i += 1
                continue

            peak = 1
            # increasing
            while i < n and ratings[i] > ratings[i-1]:
                peak += 1
                sum = sum + peak
                i += 1

            down = 0
            # decreasing
            while i < n and ratings[i] < ratings[i-1]:
                down += 1
                sum = sum + down
                i += 1

            # correction for the peak
            down += 1
            if down > peak:
                sum = sum + (down - peak)
        
        return sum