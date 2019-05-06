# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrder(root):
    # check init root is empty or not
    if not root:
        return []
    # init return array and 1st level (root)
    ans, level = [], [root]
    while level:
        # add all values from the current level
        ans.append([node.val for node in level])
        # list for next level
        temp = []
        # generate nodes for next level
        for node in level:
            temp.extend([node.left, node.right])
        # IMPORTANT: reset level as the leaves of 
        # the prev root for next iteration 
        # if no leaves, return empty list
        level = [leaf for leaf in temp if leaf]
    return ans

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(levelOrder(root))