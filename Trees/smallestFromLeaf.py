'''
Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def smallestFromLeaf(root):
    def dfs(node, path):
        if not node: return
        path.append(chr(ord('a')+node.val))
        if not node.left and not node.right:
            res[0] = min(res[0], ''.join(path)[::-1])
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        path.pop()
    
    res = [str(chr(ord('z') + 1))]
    dfs(root, [])
    return res[0]