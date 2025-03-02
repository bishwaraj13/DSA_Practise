# https://leetcode.com/problems/search-a-2d-matrix/
from typing import *

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def find_row():
            if ROWS == 1:
                return 0

            left = 0
            right = ROWS - 1
            while left <= right:
                mid = (left + right) // 2
                
                if target < matrix[mid][0]:
                    right = mid - 1
                elif target > matrix[mid][COLS-1]:
                    left = mid + 1
                else:
                    return mid
            return -1

        row = find_row()
        if row == -1:
            return False

        # we now know which row to find target in
        l = 0
        r = COLS -1

        while l <= r:
            mid = (l + r) // 2

            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
        
        return False
        