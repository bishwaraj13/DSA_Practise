# https://leetcode.com/problems/rotate-list/
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        # step 1: find length of the list and pointer to tail
        tail = head

        # n is size of linkedlist
        n = 1

        while tail.next:
            tail = tail.next
            n += 1

        # step 2: find actual k
        # because if n = 5, and k = 15,
        # it means it brings it down to initial state after rotation
        # meaning real_k = 15 % 5 = 0
        real_k = k % n

        # step 3: make it circular linkedlist
        tail.next = head

        # step 4: rotation means end of linked list would be at (n-k)th node
        # and head would be the next node to it
        temp = head
        # we are already at first node, so subtracting 1
        traversal_steps = n - real_k - 1

        while traversal_steps:
            temp = temp.next
            traversal_steps -= 1

        # step 5: point temp to None, and node next to temp is new head
        head = temp.next
        temp.next = None

        return head