# https://leetcode.com/problems/palindrome-linked-list/
# There are easier way to do this using Stack which would make space complexity to O(n)
# But this is a hard but interesting solution that reduced space complexity
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # step 1: find middle node - O(n/2)
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is the middle node
        # step 2: reverse the array from middle to last node
        slow_2 = None
        fast_2 = slow
        if not slow.next:
            # there is no more node post the middle one
            # so reversal means nothing
            slow_2 = slow
        else:
            while fast_2:
                temp = fast_2.next
                fast_2.next = slow_2

                slow_2 = fast_2
                fast_2 = temp

        # slow_2 is now tail of the linkedlist
        # step 2: two pointers from both end
        left = head
        right = slow_2

        while left and right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True