# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
from typing import *

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # start at coord (0, COL-1)
        row = 0
        col = COLS-1  

        while row < ROWS and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1

        return False