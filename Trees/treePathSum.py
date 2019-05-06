# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pathSum(root, s):
    # check c++ version
    if not root: return []
    if root.left == None and root.right == None:
        if s == root.val: 
            return [[root.val]]
        else: 
            return []
    a = pathSum(root.left, s - root.val) + pathSum(root.right, s - root.val)
    return [[root.val] + i for i in a]

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

print(pathSum(root, s=22))