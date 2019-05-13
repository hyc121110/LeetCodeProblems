# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetricTree(root):
  # recursive solution
  def isMirror(p, q):
    # 1) both subtrees are null -> symmetric
    if not p and not q: return True

    # 2) not balanced -> not symmetric
    elif not p or not q: return False

    # 3) both subtress are not null
    # a) both node are the same
    # b) left.left = right.right
    # c) left.right = right.left
    # must satisfy all 3 conditions to return true
    return (p.val == q.val) and isMirror(p.left, q.right) and isMirror(p.right, q.left)
  # if not root: return True
  return not root or isMirror(root.left, root.right)

  # iterative
    
    
    

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(isSymmetricTree(root))