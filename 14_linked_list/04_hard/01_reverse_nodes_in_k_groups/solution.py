# https://leetcode.com/problems/reverse-nodes-in-k-group/
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = head

        while temp:
            # step 1: find kth node
            kth_node = self.find_kth_node(temp, k)
            if not kth_node:
                # its the last few nodes in LL
                if prev_node:
                    prev_node.next = temp
                break

            # step 2: preserve next node link and break the next link of kth node
            next_node = kth_node.next
            kth_node.next = None

            # step 3: reverse the list of kth nodes
            self.reverse_list(temp)
            if temp == head:
                # step 3A: if it was first k nodes,
                # point head to kth_node
                head = kth_node
            else:
                # step 3B: if its regular k nodes,
                # point prev_node.next to kth_node
                prev_node.next = kth_node

            # iterate for next temp
            prev_node = temp
            temp = next_node

        return head
    
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

    def find_kth_node(self, temp, k):
        k -= 1

        while temp and k > 0:
            k -= 1
            temp = temp.next

        return temp