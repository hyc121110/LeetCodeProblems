'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2
    
node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = ListNode(4)

node2 = ListNode(1)
node2.next = ListNode(3)
node2.next.next = ListNode(4)

print(mergeTwoLists(node1, node2))