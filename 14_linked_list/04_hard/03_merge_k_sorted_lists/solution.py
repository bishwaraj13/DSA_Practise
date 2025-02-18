# https://leetcode.com/problems/merge-k-sorted-lists/
import heapq
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListNodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for node in lists:
            if node:
                heapq.heappush(heap, ListNodeWrapper(node)) # O(log n)

        # create dummy node
        dummyNode = ListNode(float("-inf"))
        curr = dummyNode

        while heap:
            listNodeWrapper = heapq.heappop(heap) # O(log n)
            node = listNodeWrapper.node
            curr.next = node
            # insert node.next to heap
            node = node.next
            if node:
                heapq.heappush(heap, ListNodeWrapper(node)) # O(log n)
            curr = curr.next

        return dummyNode.next
        