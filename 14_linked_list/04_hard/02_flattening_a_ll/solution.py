# https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

class Solution:
    def flatten(self, root):
        if not root or not root.next:
            return root
            
        return self.merge_two_vertical_ll(
                root,
                self.flatten(root.next)
            )
        
    def merge_two_vertical_ll(self, list1, list2):
        # create dummy node
        dummyNode = Node(-99)
        curr = dummyNode
        
        while list1 and list2:
            if list1.data < list2.data:
                curr.bottom = list1
                list1 = list1.bottom
            else:
                curr.bottom = list2
                list2 = list2.bottom
            # make sure we break the next link,
            # because we are flattening to vertical ll
            curr.next = None
            # move to next
            curr = curr.bottom
            
        if list1:
            curr.bottom = list1
            
        if list2:
            curr.bottom = list2

        return dummyNode.bottom