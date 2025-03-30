# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers
from typing import *

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for i in range(n):
            row_set = set()
            col_set = set()

            for j in range(n):
                # check row
                if matrix[i][j] < 1 or matrix[i][j] > n or matrix[i][j] in row_set:
                    return False
                row_set.add(matrix[i][j])

                # check column
                if matrix[j][i] < 1 or matrix[j][i] > n or matrix[j][i] in col_set:
                    return False
                col_set.add(matrix[j][i])

        return True