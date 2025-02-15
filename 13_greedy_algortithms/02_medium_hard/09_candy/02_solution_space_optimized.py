# https://leetcode.com/problems/candy/
from typing import *

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left_to_right = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left_to_right[i] = left_to_right[i-1] + 1

        for j in range(n-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                left_to_right[j] = max(left_to_right[j], left_to_right[j+1] + 1)
                
        return sum(left_to_right)