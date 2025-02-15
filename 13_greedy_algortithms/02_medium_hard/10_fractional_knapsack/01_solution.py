# https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, val, wt, capacity):
        #code
        value_wt = list(zip(val, wt))
        value_wt.sort(key=lambda x: x[0] / x[1], reverse=True)

        max_val = 0
        i = 0
        remaining_capacity = capacity
        
        while remaining_capacity > 0 and i < len(value_wt):
            v, w = value_wt[i]
            
            if w > remaining_capacity:
                # 1 unit of weight's val
                w_1u = v/w
                max_val += w_1u * remaining_capacity
                remaining_capacity = 0
            else:
                remaining_capacity -= w
                max_val += v
            
            i += 1
            
        return round(max_val, 6)