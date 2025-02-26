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

    # base condition
    i = r - 1
    for j1 in range(c):
        for j2 in range(c):
            if j1 == j2:
                dp[i][j1][j2] = grid[i][j1]
            else:
                dp[i][j1][j2] = grid[i][j1] + grid[i][j2]

    for i in range(r-2, -1, -1):
        for j1 in range(c):
            for j2 in range(c):
                next_inc = [-1, 0, 1]
                maxi = float("-inf")

                for delta_1 in next_inc:
                    for delta_2 in next_inc:
                        j1_next = j1 + delta_1
                        j2_next = j2 + delta_2

                        if j1_next < 0 or j2_next < 0 or j1_next > c-1 or j2_next > c-1:
                            continue

                        if j1 == j2:
                            maxi = max(maxi, grid[i][j1] + dp[i+1][j1_next][j2_next])
                        else:
                            maxi = max(maxi, grid[i][j1] + grid[i][j2] + dp[i + 1][j1_next][j2_next])

                dp[i][j1][j2] = maxi

    # bob starts at [0][0][m-1], so we return this val
    return dp[0][0][c-1]
