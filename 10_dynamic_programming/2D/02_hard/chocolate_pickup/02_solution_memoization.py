# https://www.naukri.com/code360/problems/ninja-and-his-friends_3125885
from os import *
from sys import *
from collections import *
from math import *

from typing import List


def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    r = len(grid)
    c = len(grid[0])
    # 3d matrix for dp
    dp = [[[float("-inf") for _ in range(c)] for _ in range(c)] for _ in range(r)]

    def dfs(i, j1, j2):
        if j1 < 0 or j2 < 0 or j1 > c - 1 or j2 > c - 1:
            return 0

        if i == r - 1:
            if j1 == j2:
                return grid[i][j1]
            else:
                return grid[i][j1] + grid[i][j2]
            
        if dp[i][j1][j2] != float("-inf"):
            return dp[i][j1][j2]

        next_inc = [-1, 0, 1]
        maxi = float("-inf")

        for delta_1 in next_inc:
            for delta_2 in next_inc:
                j1_next = j1 + delta_1
                j2_next = j2 + delta_2

                if j1 == j2:
                    maxi = max(maxi, grid[i][j1] + dfs(i+1, j1_next, j2_next))
                else:
                    maxi = max(maxi, grid[i][j1] + grid[i][j2] + dfs(i + 1, j1_next, j2_next))

        dp[i][j1][j2] = maxi
        return dp[i][j1][j2]

    return dfs(0, 0, c-1)