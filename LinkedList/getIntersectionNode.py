'''
Write a program to find the node at which the intersection of two singly linked lists begins.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''

'''
We can use two iterations to do that. In the first iteration, we will reset the pointer of one linkedlist to the head of another linkedlist after it reaches the tail node. In the second iteration, we will move two pointers until they points to the same node. Our operations in first iteration will help us counteract the difference. So if two linkedlist intersects, the meeting point in second iteration must be the intersection point. If the two linked lists have no intersection at all, then the meeting pointer in second iteration must be the tail node of both lists, which is null

Regardless of the length of the two lists, the sum of the lengths are the same (i.e. a+b = b+a), which means that the pointers sync up at the point of intersection.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
  if not headA or not headB: return None
  
  a = headA
  b = headB

  while a != b:
    a = headB if not a else a.next
    b = headA if not b else b.next

  return a

head1 = ListNode(4)
head1.next = ListNode(1)
head1.next.next = ListNode(8)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

head2 = ListNode(5)
head2.next = ListNode(0)
head2.next.next = ListNode(1)
head2.next.next.next = ListNode(8)
head2.next.next.next.next = ListNode(4)
head2.next.next.next.next.next = ListNode(5)

node = getIntersectionNode(head1, head2)
print(node.val)