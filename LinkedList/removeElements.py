'''
Remove all elements from a linked list of integers that have value val.
'''

def removeElements(self, head, val):
  # check head.val is equal to val, if equals, move pointer until not equal
  while head is not None and head.val == val:
    head = head.next
  # if head.val != val, check head.next.val == val, if equals, adjust pointers
  current = head
  while current is not None:
    if current.next is not None and current.next.val == val:
      current.next = current.next.next
    else:
      current = current.next
  return head