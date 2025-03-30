# https://leetcode.com/problems/hand-of-straights/
from typing import *
from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Step 1: Check if the length is divisible by groupSize
        if len(hand) % groupSize != 0:
            return False
        
        # Step 2: Count frequencies of each card
        count = Counter(hand)
        
        # Step 3: Create a min-heap with unique card values
        min_heap = list(count.keys())
        heapq.heapify(min_heap)
        
        # Step 4: Form groups of consecutive cards
        while min_heap:
            # Get the smallest card value
            start = min_heap[0]
            
            # Try to form a group of consecutive cards
            for i in range(start, start + groupSize):
                # If the current card doesn't exist or has been used up
                if i not in count or count[i] == 0:
                    return False
                
                # Decrease the count of the current card
                count[i] -= 1
                
                # If the count becomes zero, remove it from the heap
                if count[i] == 0 and i == min_heap[0]:
                    heapq.heappop(min_heap)
        
        return True