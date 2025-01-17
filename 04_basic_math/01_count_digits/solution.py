# https://www.geeksforgeeks.org/problems/count-digits5716/1
class Solution:
    def evenlyDivides(self, n):
        quotient = n
        count = 0
        
        while (quotient > 0):
            digit = quotient % 10
            
            if digit != 0 and n % digit == 0:
                count += 1
                
            quotient = quotient // 10
            
        return count