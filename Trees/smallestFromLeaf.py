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