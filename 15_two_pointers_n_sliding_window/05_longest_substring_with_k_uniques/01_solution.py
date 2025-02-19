# http://geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1
class Solution:

    def longestKSubstr(self, s, k):
        l = 0
        r = 0
        max_len = -1
        hashmap = {}
        
        while r < len(s):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            
            while len(hashmap) > k:
                hashmap[s[l]] -= 1
                
                if hashmap[s[l]] == 0:
                    del hashmap[s[l]]
                    
                l += 1
            
            if len(hashmap) == k:  
                max_len = max(max_len, r-l+1)
            r += 1
            
        return max_len