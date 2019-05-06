'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    # base case: root return None
    if not root: 
        return None
    # check if root.val is the value we are looking for (p or q)
    if root.val == p.val or root.val == q.val: 
        return root
    # neither are satisfied: perform search on left and right subtrees
    leftSubtreeResult = lowestCommonAncestor(root.left, p, q)
    rightSubtreeResult = lowestCommonAncestor(root.right, p, q)
    # at this stage if left or right subtree is None, return right or left subtree respectively because base cases will hit meaning we find either p or q in one of the subtrees
    if not leftSubtreeResult: 
        return rightSubtreeResult
    if not rightSubtreeResult: 
        return leftSubtreeResult
    # left and right subtrees both not None, we found the LCA!
    return root

root = TreeNode(3)

root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

node = lowestCommonAncestor(root, TreeNode(5), TreeNode(1))
print(node.val)