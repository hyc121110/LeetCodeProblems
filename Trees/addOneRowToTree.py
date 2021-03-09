"""
Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution 1: DFS
"""
We could definitely solve this a number of ways, but I'm always partial to recursion when possible, especially when you can simply recurse the main function rather than having to define a separate recursive helper function. The recursive route is a depth-first search (DFS) solution.

We can use the depth variable (d) as a countdown of sorts, decrementing it as we traverse downward through the tree until we get to our destination row. Since we're going to need to attach the new nodes at d to their parents, we should actually perform our operations when d = 2, rather than d = 1, so that we have access to the parent node.

This also allows us to deal with the sticky edge case of when the original value of d is 1. Since no parent exists for the original root, we'll have to just create our new node and attach the root to it before returning. This can only ever happen on the initial function call, as otherwise we will never reach d = 1 in any later recursion.

The function will return the node each recursion, but since we're not doing anything with the return value when the the function is called internally, it will only really be meaningful on the original function call.

This works because we're passing node references through the recursion, so the tree object is being modified regardless of return values.
"""
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v, root, None)
        elif d == 2:
            root.left = TreeNode(v, root.left, None)
            root.right = TreeNode(v, None, root.right)
        else:
            if root.left: self.addOneRow(root.left, v, d-1)
            if root.right: self.addOneRow(root.right, v, d-1)
            
        return root
    
# solution 2: BFS (advanced)
# using dummy node
class Solution2:
    def addOneRow(self, root, v, d):
        dummy, dummy.left = TreeNode(None), root
        row = [dummy]
        for _ in range(d - 1):
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        for node in row:
            node.left, node.left.left = TreeNode(v), node.left
            node.right, node.right.right = TreeNode(v), node.right
        return dummy.left