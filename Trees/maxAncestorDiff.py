'''
Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxAncestorDiff(root):
    def dfs(root, mx, mn):
        if not root: # base case
            return 0
        mx = max(root.val, mx) # update max
        mn = min(root.val, mn) # update min
        l = dfs(root.left, mx, mn) # recurse down
        r = dfs(root.right, mx, mn) # recurese down
        return max(mx - mn, max(l, r)) # compare all super/sub differences to get result.
    
    return dfs(root, root.val, root.val)
    
root = TreeNode(8)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)

root.right = TreeNode(10)
root.right.left = TreeNode(9)
root.right.right = TreeNode(14)

print(maxAncestorDiff(root))