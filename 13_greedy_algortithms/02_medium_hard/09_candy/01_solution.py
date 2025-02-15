# https://leetcode.com/problems/candy/
from typing import *

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left_to_right = [1] * n
        right_to_left = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left_to_right[i] = left_to_right[i-1] + 1
        
        for j in range(n-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                right_to_left[j] = right_to_left[j+1] + 1

        count = 0
        for i, j in zip(left_to_right, right_to_left):
            count += max(i, j)

        return count