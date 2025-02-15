# https://leetcode.com/problems/non-overlapping-intervals/
from typing import *

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        next_non_overlap = float("-inf")

        interval_removed_count = 0

        for interval_start, interval_end in intervals:
            if interval_start >= next_non_overlap:
                next_non_overlap = interval_end
            else:
                interval_removed_count += 1

        return interval_removed_count