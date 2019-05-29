'''
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
  if not head: return False
  # initialize two pointers 
  slow = head
  fast = head

  # continue until end of list or until we find a cycle
  while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next
    if slow.val == fast.val:
      return True
  
  return False

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

print(hasCycle(head))