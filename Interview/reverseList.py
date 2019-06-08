'''
Reverse a singly linked list.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# similar to reverseBetween
def reverseList(head):
  # iterative
  # two pointers: cur, prev
  prev = None
  # cur = None

  while head:
    # 1st set cur to head
    # 2nd set head to the next node
    # 3rd cur.next is the previous node
    # 4th set prev for the next cur.next (reverse)
    cur = head
    head = head.next
    cur.next = prev
    prev = cur
    # cur, head, cur.next, prev = head, head.next, prev, cur

  return prev

  # recursion
  # def _reverse(node, prev=None):
  #   if not node:
  #     return prev
  #   n = node.next
  #   node.next = prev
  #   return _reverse(n, node)
  
  # return _reverse(head)



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(reverseList(head))