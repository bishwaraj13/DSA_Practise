# https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class Solution:
    def reverseDLL(self, head):
        # case 1: no head
        if not head:
            return None
          
        # case 2: only 1 node  
        if not head.next:
            return head
         
        # case 3: regular cases   
        curr = head
        
        while curr:
            last = curr.prev
            curr.prev = curr.next
            curr.next = last
            
            # to go to next node,
            # we need to go to curr.prev
            # because we reversed the link
            curr = curr.prev
            
        return last.prev