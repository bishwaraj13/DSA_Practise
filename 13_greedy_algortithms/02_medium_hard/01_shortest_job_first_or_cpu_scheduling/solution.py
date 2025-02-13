# https://www.geeksforgeeks.org/problems/shortest-job-first/1
class Solution:
    def solve(self, bt):
        waiting_time = [0] * len(bt)
        bt.sort()
        
        for i in range(len(bt)):
            if i == 0:
                continue
            waiting_time[i] = waiting_time[i-1] + bt[i-1]
            
        return sum(waiting_time) // len(waiting_time)