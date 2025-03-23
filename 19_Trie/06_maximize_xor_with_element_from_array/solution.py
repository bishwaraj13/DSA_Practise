# https://leetcode.com/problems/maximum-xor-with-an-element-from-array/
from typing import *

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
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Sort the nums array
        nums.sort()
        
        # Add index to queries for retrieving original order
        indexed_queries = [(x, m, i) for i, (x, m) in enumerate(queries)]
        # Sort queries by m (the maximum allowed value)
        indexed_queries.sort(key=lambda q: q[1])
        
        n = len(nums)
        m = len(queries)
        answer = [-1] * m  # Initialize with -1
        
        trie = Trie()
        nums_index = 0  # To keep track of inserted numbers
        
        for x, m, original_index in indexed_queries:
            # Insert all numbers <= m into the trie
            while nums_index < n and nums[nums_index] <= m:
                trie.insert(nums[nums_index])
                nums_index += 1
            
            # If we inserted at least one number, find max XOR
            if nums_index > 0 and nums[0] <= m:
                answer[original_index] = trie.find_max_xor(x)
            # Otherwise, answer remains -1
        
        return answer