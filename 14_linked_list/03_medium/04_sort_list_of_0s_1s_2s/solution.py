# https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        if not head or not head.next:
            return head
            
        temp = head
        zeroHead = Node(-1)
        zeroTemp = zeroHead
        oneHead = Node(-1)
        oneTemp = oneHead
        twoHead = Node(-1)
        twoTemp = twoHead
        
        while temp:
            if temp.data == 0:
                zeroTemp.next = temp
                zeroTemp = temp
            elif temp.data == 1:
                oneTemp.next = temp
                oneTemp = temp
            else:
                twoTemp.next = temp
                twoTemp = temp
                
            temp = temp.next

        # draw and check.. this takes care of the cases:
        # if both zeroHead and twoHead are None.
        # Also, tbh the condition below are hard to come up with
        if oneHead.next:
            zeroTemp.next = oneHead.next
        else:
            zeroTemp.next = twoHead.next
            
        if twoHead.next:
            oneTemp.next = twoHead.next
            
        # Cleanup (not required)
        twoHead.next = None
            
        return zeroHead.next