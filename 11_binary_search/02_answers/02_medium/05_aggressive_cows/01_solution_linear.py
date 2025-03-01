# https://www.geeksforgeeks.org/problems/aggressive-cows/0
class Solution:
    def aggressiveCows(self, stalls, k):
        def canWePlace(dist, total_cows):
            countCows = 1
            last_placed = stalls[0]
            
            for i in range(1, len(stalls)):
                if stalls[i] - last_placed >= dist:
                    countCows += 1
                    last_placed = stalls[i]
                    
            if countCows >= total_cows:
                return True
            return False
            
        # sort the stalls
        stalls.sort()
        
        min_dist = 1
        max_dist = stalls[-1] - stalls[0]
        
        for i in range(min_dist, max_dist + 1):
            if canWePlace(i, k):
                continue
            else:
                return i-1