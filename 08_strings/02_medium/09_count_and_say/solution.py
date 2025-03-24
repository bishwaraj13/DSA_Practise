# https://leetcode.com/problems/count-and-say/description/
class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"
        
        # Get the previous term in the sequence
        prev = self.countAndSay(n - 1)
        
        result = ""
        count = 1
        
        # Iterate through the previous term
        for i in range(1, len(prev) + 1):
            # If current character is the same as previous, increase count
            if i < len(prev) and prev[i] == prev[i - 1]:
                count += 1
            else:
                # Add the count and the digit to the result
                result += str(count) + prev[i - 1]
                # Reset count for the next unique digit
                count = 1
                
        return result