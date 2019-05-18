'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def rightSideView(root):
  # dfs
  # def collect(node, depth):
  #   if node:
  #     # this condition makes sure only 1 node per level
  #     if depth == len(view):
  #       view.append(node.val)
  #     # traverse to right tree first as right subtree having the priority
  #     collect(node.right, depth+1)
  #     collect(node.left, depth+1)
  # view = []
  # collect(root, 0)
  # return view
  # iterative
  explored = set([])
  res = []
  if not root:
    return res
  
  # pair: root, level
  stack = [(root,0)]
  
  while stack:
    node, level = stack.pop()
    # don't add node if level already explored
    if level not in explored:
      explored.add(level)
      res.append(node.val)
    # stack left then right ensures the first item being popped is right (only if right is empty)
    if node.left:
      stack.append((node.left, level+1))
    if node.right:
      stack.append((node.right, level+1))
  return res

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
print(rightSideView(root))