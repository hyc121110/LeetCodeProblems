# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(root):
    # method 1: recursive solution
    # if not root: return []
        
    # def helper(curr, res):
    #     if curr:
    #         helper(curr.left, res)
    #         res.append(curr.val)
    #         helper(curr.right, res)
    # res = []
    # helper(root, res)
    
    # return res

    # method 2: iterative solution
    # use a stack to store the current node
    res, stack = [], [(root, False)]

    while stack:
        cur, visited = stack.pop()
        # only process not None nodes
        if cur:
            if not visited:
                # push cur and its children in reverse order
                # note: if cur.children returns None, we have reached the end and also because we set visited to true, we can push the node to res
                stack.append((cur.right, False))
                # now we visited the cur node
                stack.append((cur, True))
                stack.append((cur.left, False))
            else:
                res.append(cur.val)
    return res

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(inorderTraversal(root))