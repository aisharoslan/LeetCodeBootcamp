#Hard
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Brute Force 
# Traverse all linked lists and collect values of nodes into an array
# Sort and iterate over this array
# Create new sorted LL with new nodes
class Solution:
    def mergeKLists(self, lists):
        nodes = [] #to store all elem
        head = point = ListNode(0) #creates head node with value = 0
        for l in lists: #O(n)
            while l: #while non-empty list
                nodes.append(l.val) 
                l = l.next
        
        for val in sorted(nodes): #O(nlogn) + O(n)
            point.next = ListNode(val) # to create new LL
            point = point.next

        return head.next

# Time: O(nlogn) - n is total no. of nodes, collecting all values is O(n), stable sorting algo is O(nlogn), iterating costs O(n)    
# Space: O(n)