# https://leetcode.com/problems/reverse-linked-list/
from typing import *

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        reversed_head = self.reverseList(head.next)
        # get last node of reversed list
        # which is now actually the node pointed by head
        last_node = head.next

        # reverse it
        last_node.next = head
        head.next = None

        return reversed_head