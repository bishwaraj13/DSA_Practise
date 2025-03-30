# https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a hash map to count frequencies of characters in magazine
        char_counts = {}
        
        # Count each character in magazine
        for char in magazine:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        
        # Check if we have enough of each character for ransomNote
        for char in ransomNote:
            # If the character doesn't exist in magazine or count becomes negative
            if char not in char_counts or char_counts[char] <= 0:
                return False
            # Decrease the count as we use the character
            char_counts[char] -= 1
            
        # If we get here, we had enough of each character
        return True