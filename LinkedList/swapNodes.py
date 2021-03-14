"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# solution1
# Time Complexity : O(N), required for iterating over the linked list, where N is the number of nodes in linked list.
# Space Complexity : O(1), since only constant space is used.
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # first iteration: find length of linked list
        _len = 0
        iteration = head
        while iteration:
            iteration = iteration.next
            _len += 1
        
        # second iteration: assign kth node and kth node from end
        iteration = head
        idx = 0
        kth_from_start = None
        kth_from_end = None
        while iteration:
            if idx == k-1:
                kth_from_start = iteration
            if idx == _len - k:
                kth_from_end = iteration
            if kth_from_start and kth_from_end:
                break
            iteration = iteration.next
            idx += 1
        
        # swap
        kth_from_start.val, kth_from_end.val = kth_from_end.val, kth_from_start.val
            
        return head

# solution 2: 
# Time Complexity : O(N) While this complexity is same as previous, the constant factor is reduced by half.
# Space Complexity : O(1), since only constant space is used.
class Solution2:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        kth_from_end = head
        _iter = head
        
        k -= 1
        while k and _iter.next:
            _iter = _iter.next
            k -= 1
        
        kth_from_start = _iter
        
        while _iter.next:
            _iter = _iter.next
            kth_from_end = kth_from_end.next
            
        kth_from_end.val, kth_from_start.val = kth_from_start.val, kth_from_end.val
        return head