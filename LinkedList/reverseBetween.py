'''
Reverse a linked list from position m to n. Do it in one-pass.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseBetween(head, m, n):
  if m == n:
    return head

  # dummy node for later
  # p: for relinking nodes
  dummy = p = ListNode(0)
  dummy.next = head

  # set prev pointer to one node just before the mth node
  for _ in range(m-1):
    p = p.next

  cur, prev = p.next, None

  # reverse nodes (n-m+1) times
  # 1st iter: prepare prev and cur pointers to right position
  for _ in range(n-m+1):
    cur.next, prev, cur = prev, cur, cur.next  # REMEMBER THIS SWITCH PATTERN!

  # since p.next.next now one node before cur, relink them
  p.next.next = cur
  # p.next is just the nth item before reverse (Now prev)
  p.next = prev

  return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(reverseBetween(head, m=2, n=4))