# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        if not head.next:
            if n == 1:
                return None
            else:
                return head

        slow = head
        fast = head

        while n > 0 and fast:
            fast = fast.next
            n -= 1

        # this is an edge case.
        # e.g, we have n nodes only, and
        # we are asked to delete nth node from last
        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head