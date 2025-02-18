# https://leetcode.com/problems/sort-list/
# Did merge sort but on Linked List
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        middle = self.middleNode(head)
        leftHead = head
        rightHead = middle.next

        # separate out it into two halves
        middle.next = None

        leftList = self.sortList(leftHead)
        rightList = self.sortList(rightHead)

        return self.mergeTwoLists(leftList, rightList)

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy node
        newNode = ListNode(-99)
        curr = newNode

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1

        if list2:
            curr.next = list2

        return newNode.next