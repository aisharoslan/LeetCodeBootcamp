#Easy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Approach 1: Fast & Slow Pointers (BEST)
class Solution:
    def hasCycle(self, head) -> bool:
        if head is None: #edge case if head is empty
            return False
            
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

#Time: O(n)
#Space: O(1)

#Approach 2: Hashing (Time: O(n), Space: O(n))
class Solution:
    def hasCycle(self, head) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False


