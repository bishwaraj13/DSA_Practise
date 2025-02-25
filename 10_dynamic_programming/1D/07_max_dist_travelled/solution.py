'''
Maximum Distance with Energy Constraints
    
Problem Description
You are given an array distances[n] representing the possible distances you can travel on each day, where n is the number of days. You also have an energy level K that determines whether you can travel on a given day.
The rules are:
If you choose to travel on day i, you will cover distances[i] units and your energy (K) decreases by 1
If you choose to rest on day i, you don't travel any distance but your energy (K) increases by 1
You cannot travel if your energy (K) is 0
Maximum value of K cannot exceed the initial given value
Return the maximum total distance you can travel over the n days.

Example 1:
Input: 
distances = [20, 10, 2, 5, 50, 15, 13]
n = 7
k = 3

output = 108

Explanation: 
Day 1: Travel 20 units (K: 3 → 2)
Day 2: Travel 10 units (K: 2 → 1)
Day 3: Rest (K: 1 → 2)
Day 4: Rest (K: 2 → 3)
Day 5: Travel 50 units (K: 3 → 2)
Day 6: Travel 15 units (K: 2 → 1)
Day 7: Travel 13 units (K: 1 → 0)
Total distance = 20 + 10 + 50 + 15 + 13 = 108
'''
from typing import list

class Solution:
    def maximumTotalDistance(self, distances: List[int], k: int):
        def dfs(i, energy):
            # base condition
            if i == 0 and energy > 0:
                return distances[i]
            
            if i == 0 and energy <= 0:
                return 0
            
            work = float("-inf")
            rest = float("-inf")

            if energy > 0:
                # you may choose to work
                work = distances[i] + dfs(i-1, energy-1)

            # you may rest
            # update energy
            energy = min(k, energy+1)
            rest = dfs(i-1, energy)

            return max(work, rest)
        
        return dfs(len(distances)-1, k)
    
print(Solution().maximumTotalDistance([20, 10, 2, 5, 50, 15, 13], 3))
