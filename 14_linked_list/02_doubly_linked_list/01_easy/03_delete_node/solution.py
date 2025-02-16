# https://www.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1
class Solution:
    def delete_node(self, head, x):
        if x == 1:
            head.next.prev = None
            return head.next
            
        temp = head
        pos = 1
        
        while pos < x:
            temp = temp.next
            pos += 1
            
        prevNode = temp.prev
        if prevNode:
            prevNode.next = temp.next
            
        nextNode = temp.next
        if nextNode:
            nextNode.prev = prevNode
            
        return head