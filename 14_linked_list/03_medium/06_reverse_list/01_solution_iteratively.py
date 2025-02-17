# https://leetcode.com/problems/reverse-linked-list/
from typing import *

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        slow = None
        fast = head

        while fast:
            temp = fast.next
            fast.next = slow

            slow = fast
            fast = temp

        return slow