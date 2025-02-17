# https://leetcode.com/problems/linked-list-cycle-ii/
# Explanation requires drawing one example, and following this derivation:
# If the starting point of loop is at distance x from head, cycle length is c and the point where slow and fast meet is at distance y from the starting point, as we know the slow and fast starts at head and slow moves by 1 and fast moves by 2 from the start, we can say, 
# 2*distance traveled by slow pointer = distance traveled by fast pointer.
# ==> 2*(x+y) = x + c + y   ==> x = c-y
# Thus we can say that the distance of head to start of the loop is the same as the fast to start point of the loop.
# So if we update slow by head, and move slow and fast simultaneously then the point where we meet is the start point of the loop.
from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        # if the loop ended because of any other reason,
        # we should return None
        if slow != fast:
            return None

        # now we should start slow pointer from head,
        # and fast pointer from collision point..
        # and the place they meet again, will be start of loop
        slow = head

        while slow != fast:
            slow = slow.next
            # in this loop, we only move fast by one step
            fast = fast.next

        return slow
