# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
val = 0
def bstToGst(root):
    if root.right: self.bstToGst(root.right)
    root.val = self.val = self.val + root.val
    if root.left: self.bstToGst(root.left)
    return root

root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)

root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

node = bstToGst(root)
print(node.val)
#print(node)