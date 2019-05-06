'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def addTwoNumbers(self,l1,l2):
        carry = 0
        # start from a random node
        root = n = ListNode(0)
        while l1 or l2 or carry:
            # init v1 v2 to 0 in case length of l1, l2 are unequal
            v1 = v2 = 0
            # check if l1, l2 is None or not
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            # calculate carry and value using divmod
            carry, val = divmod(v1+v2+carry, 10)
            # update return value and its next node
            n.next = ListNode(val)
            n = n.next
        # return from random.next
        return root.next

l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)
l4 = ListNode(5)
l5 = ListNode(6)
l6 = ListNode(4)
l1.next = l2
l2.next = l3
l4.next = l5
l5.next = l6
l7 = ListNode(0)

result = l7.addTwoNumbers(l1,l4)
while result.next:
    print(result.val)
    result = result.next