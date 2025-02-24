# https://www.naukri.com/code360/problems/ninja-s-training_3621003
from typing import *

def ninjaTraining(n: int, points: List[List[int]]) -> int:
    # last = 0 means 0th task was done
    # last = 3 means no task was done
    # initial call for f(n-1, 3)
    def dfs(day, last):
        # 0th day will be stopping point considering we are starting from n-1
        if day == 0:
            maxi = 0
            # iterate over all the tasks
            for i in range(3):
                if i != last:
                    maxi = max(maxi, points[0][i])

            return maxi

        maxi = 0
        for i in range(3):
            if i != last:
                points_earned = points[day][i] + dfs(day-1, i)
                maxi = max(maxi, points_earned)

        return maxi

    return dfs(len(points)-1, 3)
