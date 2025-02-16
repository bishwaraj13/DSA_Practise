# https://leetcode.com/problems/add-two-numbers/
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        carry = 0
        head = None
        prev = head

        while temp1 or temp2 or carry:
            total = carry
            if temp1:
                total += temp1.val
                temp1 = temp1.next

            if temp2:
                total += temp2.val
                temp2 = temp2.next

            # value for this linkedlist
            #least significant bit: 
            l = total % 10

            if not head:
                head = ListNode(l)
                prev = head
            else:
                prev.next = ListNode(l)
                prev = prev.next

            carry = (total - l) // 10

        return head