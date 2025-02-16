# https://leetcode.com/problems/odd-even-linked-list/description/
from typing import *

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        odd = head
        even = head.next
        even_head = head.next

        # if even can't reach, odd also wont reach
        # so condition is based on even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = even_head

        return head