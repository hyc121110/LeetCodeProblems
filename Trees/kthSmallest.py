'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def kthSmallest(root, k):
  # iterative: stack the nodes in ascending order (root.left)
  stack = []
  while True:
    # stacked all nodes on the left
    while root:
      stack.append(root)
      root = root.left
    # left done, check root node
    root = stack.pop()
    # root check. see if it is the kth smallest
    k -= 1
    if k == 0:
      return root.val
    # check right subtree
    root = root.right

root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(4)
print(kthSmallest(root, k=1))

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
#root.left.left.left = TreeNode(1)
root.right = TreeNode(6)
print(kthSmallest(root, k=5))