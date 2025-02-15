# https://leetcode.com/problems/insert-interval/description/
from typing import *

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n = len(intervals)
        i = 0

        # list of intervals which are before the new interval,
        # and are not overlapping
        while (i < n and intervals[i][1] < newInterval[0]): 
            result.append(intervals[i])
            i += 1

        # overlapping part
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        # list of intervals which are after the new interval
        # and are non overlapping
        while i < n:
            result.append(intervals[i])
            i += 1

        return result