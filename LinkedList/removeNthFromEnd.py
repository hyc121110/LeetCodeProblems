'''
Given a linked list, remove the n-th node from the end of list and return its head.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    # idea: fast pointer creates a gap between slow pointer
    # and itself. The gap is the nth node from end of the list

    # init pointers to the start
    fast = slow = head

    # fast goes first
    for _ in range(n):
        fast = fast.next
    # fast may go beyond the list
    if not fast:
        return head.next

    while fast.next:
        # sync both pointers until fast reached the end of list
        fast = fast.next
        slow = slow.next
    # replace slow.next with the one after it
    slow.next = slow.next.next
    return head

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
print(removeNthFromEnd(head=node, n=2))