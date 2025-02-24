# https://www.naukri.com/code360/problems/ninja-s-training_3621003
from typing import *

def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp_cache = [[-1 for i in range(4)] for i in range(len(points))]
    
    # computing for day = 0
    dp_cache[0][0] = max(points[0][1], points[0][2])
    dp_cache[0][1] = max(points[0][0], points[0][2])
    dp_cache[0][2] = max(points[0][0], points[0][1])
    dp_cache[0][3] = max(points[0][0], points[0][1], points[0][2])

    # do it for day 1 to n-1
    # notice: the first two for loop is generally handled by recursion in memoization-way
    for day in range(1, len(points)):
        for last in range(3):
            dp_cache[day][last] = 0

            for task in range(3):
                # the following three lines are copy of line 25-27 of memoization technique
                if task != last:
                    points_earned = points[day][task] + dp_cache[day-1][task]
                    dp_cache[day][last] = max(dp_cache[day][last], points_earned)
            
            # update the dp_cache[day][3] with the max
            dp_cache[day][3] = max(dp_cache[day][0], dp_cache[day][1], dp_cache[day][2])

    return dp_cache[len(points)-1][3]
