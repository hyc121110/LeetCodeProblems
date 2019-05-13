'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# method similar to inorderTraversal

def binaryTreePaths(root):
  # iterative solution
  if not root:
      return []
  res, stack = [], [(root, "")]
  while stack:
    node, ls = stack.pop()
    if not node.left and not node.right:
      res.append(ls+str(node.val))
    if node.right:
      stack.append((node.right, ls+str(node.val)+"->"))
    if node.left:
      stack.append((node.left, ls+str(node.val)+"->"))
  return res

  # recursive solution
  
  # def dfs(self, root, ls, res):
  #   if not root.left and not root.right:
  #     res.append(ls+str(root.val))
  #   if root.left:
  #     self.dfs(root.left, ls+str(root.val)+"->", res)
  #   if root.right:
  #     self.dfs(root.right, ls+str(root.val)+"->", res)
  #   if not root:
  #     return []
  # res = []
  # dfs(root, "", res)
  # return res


root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(3)