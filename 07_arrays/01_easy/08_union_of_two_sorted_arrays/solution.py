# https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        a_pointer = 0
        b_pointer = 0
        c = []
        
        while a_pointer < len(a) and b_pointer < len(b):
            # skip dupliacates in 'a'
            while a_pointer+1 < len(a) and a[a_pointer] == a[a_pointer+1]:
                a_pointer += 1
                
            # skip duplicates in b
            while b_pointer+1 < len(b) and b[b_pointer] == b[b_pointer+1]:
                b_pointer += 1
                
            if a[a_pointer] < b[b_pointer]:
                c.append(a[a_pointer])
                a_pointer += 1
            elif a[a_pointer] > b[b_pointer]:
                c.append(b[b_pointer])
                b_pointer += 1
            else:
                c.append(a[a_pointer])
                a_pointer += 1
                b_pointer += 1
                
        while a_pointer < len(a):
            # skip dupliacates in 'a'
            while a_pointer+1 < len(a) and a[a_pointer] == a[a_pointer+1]:
                a_pointer += 1
                
            c.append(a[a_pointer])
            a_pointer += 1
            
        while b_pointer < len(b):
            # skip duplicates in b
            while b_pointer+1 < len(b) and b[b_pointer] == b[b_pointer+1]:
                b_pointer += 1
                
            c.append(b[b_pointer])
            b_pointer += 1
                
            
        return c
    