'''
Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  res = 0
  def distributeCoins(self, root):
    def dfs(root):
      if not root:
        return 0
      # left subtree returns total number of moves needed to change val from val to 1
      left = dfs(root.left)
      # similar to left
      right = dfs(root.right)
      # add left and right to global variable
      self.res += abs(left) + abs(right)
      # return the number of moves need to change from val to 1
      return root.val + left + right - 1

    dfs(root)
    return self.res


root = TreeNode(3)
root.left =TreeNode(0)
root.right = TreeNode(0)

sol = Solution()
print(sol.distributeCoins(root))