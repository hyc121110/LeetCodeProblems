'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
Here, pre is the previous node. Since the head doesn't have a previous node, I just use self instead. Again, a is the current node and b is the next node.

To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next, we need to change those three references. Instead of thinking about in what order I change them, I just change all three at once.

e.g dummy -> 1 -> 2 -> 3 -> 4 ---> dummy -> 2 -> 1 -> 3 -> 4
    pre is 1
    dummy -> 2 -> 1 -> 3 -> 4 ---> dummy -> 2 -> 1 -> 4 -> 3
    pre is 3
    3.next is None -> exit loop
'''
def swapPairs(head):
    dummy = pre = ListNode(0)
    pre.next = head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return dummy.next

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)

node = swapPairs(a)
print(node)