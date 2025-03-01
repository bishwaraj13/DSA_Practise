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
        result = -1
        
        low = min_dist
        high = max_dist
        
        while low <= high:
            mid = (low + high) // 2
            
            if canWePlace(mid, k):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return result
                