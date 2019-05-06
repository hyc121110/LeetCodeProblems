'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

-The left subtree of a node contains only nodes with keys less than the node's key.
-The right subtree of a node contains only nodes with keys greater than the node's key.
-Both the left and right subtrees must also be binary search trees.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isValidBST(root):
    if root is None:
        return True
    stack = []
    maximum = -float('inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root is None:
            continue
        if root.val <= maximum:
            return False
        maximum = root.val
        root = root.right
    return True

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(isValidBST(root))