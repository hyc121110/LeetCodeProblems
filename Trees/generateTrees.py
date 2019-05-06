'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def generateTrees(n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    def generate(arr):
        # if no left/right subtrees, return None
        if not arr:
            return [None]
        # init list for return
        ans = []
        # 1st loop: iterate list of possible roots
        for i in range(len(arr)):
            # generate left and right subtrees based on current root
            lefts, rights = generate(arr[:i]), generate(arr[i+1:])
            # loop through all the left nodes
            for l in lefts:
                # loop throught all the right nodes
                for r in rights:
                    root, root.left, root.right = TreeNode(arr[i]), l, r
                    ans.append(root)
        return ans

    return(generate(list(range(1,n+1)))) if n else []