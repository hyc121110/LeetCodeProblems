'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetricTree(root):
  # recursive solution
  # def isMirror(p, q):
  #   # 1) both subtrees are null -> symmetric
  #   if not p and not q: return True

  #   # 2) not balanced -> not symmetric
  #   elif not p or not q: return False

  #   # 3) both subtress are not null
  #   # a) both node are the same
  #   # b) left.left = right.right
  #   # c) left.right = right.left
  #   # must satisfy all 3 conditions to return true
  #   return (p.val == q.val) and isMirror(p.left, q.right) and isMirror(p.right, q.left)
  # # if not root: return True
  # return not root or isMirror(root.left, root.right)

  # iterative solution
  if not root: return True
  
  # init stack with root's children
  stack = [(root.left, root.right)]

  while stack:
    pair = stack.pop()
    left, right = pair[0], pair[1]
    # 1) both subtrees are null -> continue until stack empty
    if not left and not right: continue
    # 2) not balanced / value not the same -> not symmetric
    if not left and right or not right and left or left.val != right.val: return False
    # 3) both subtrees are not null -> append for check
    stack.append((left.left, right.right))
    stack.append((left.right, right.left))
  return True


root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(isSymmetricTree(root))