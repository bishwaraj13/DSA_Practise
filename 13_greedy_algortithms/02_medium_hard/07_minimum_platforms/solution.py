# https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        arr.sort()
        dep.sort()

        trains_in_platform = 0
        max_trains_simultaneously = 1
        
        l = 0
        r = 0
        
        while l < len(arr) and r < len(dep):
            if arr[l] <= dep[r]:
                # a train arrived
                # note: we took equal-to also, 
                # because even if a train departed at same time,
                # we will depart it next loop,
                # because multiple platforms required
                trains_in_platform += 1
                max_trains_simultaneously = max(max_trains_simultaneously, trains_in_platform)
                l += 1
            elif dep[r] < arr[l]:
                # a train departed
                trains_in_platform -= 1
                r += 1
                
        return max_trains_simultaneously