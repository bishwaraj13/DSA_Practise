# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
class TrieNode:
    def __init__(self):
        # Using array of size 2 instead of dictionary
        # Index 0 for bit 0, index 1 for bit 1
        self.children = [None, None]
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        # Insert num bit by bit from most significant bit (MSB)
        for i in range(31, -1, -1):  # For 32-bit integers
            bit = (num >> i) & 1
            if node.children[bit] is None:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    
    def find_max_xor(self, num):
        node = self.root
        max_xor = 0
        
        # Try to find bits that are opposite to maximize XOR
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # If we can find the opposite bit, take it to maximize XOR
            opposite_bit = 1 - bit
            
            if node.children[opposite_bit] is not None:
                max_xor |= (1 << i)  # Set this bit in result
                node = node.children[opposite_bit]
            else:
                node = node.children[bit]
        
        return max_xor

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
    
        # Insert all numbers into trie
        for num in nums:
            trie.insert(num)
        
        max_xor = 0
        # Find max XOR for each number
        for num in nums:
            max_xor = max(max_xor, trie.find_max_xor(num))
        
        return max_xor
        