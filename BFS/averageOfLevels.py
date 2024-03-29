"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        
        ret = []
        this_level = [root]
        
        while this_level:
            # get the number of nodes in the current level
            n = len(this_level)
            _sum = 0 # initialize the sum of the current level
            
            for _ in range(n): # current level iteration
                node = this_level.pop(0)
                _sum += node.val
                
                if node.left:
                    this_level.append(node.left)
                if node.right:
                    this_level.append(node.right)
            ret.append(_sum / n)
            
                
        return ret
        
# Time Complexity : O(N), where N is the number of nodes in the given Tree.
# Space Complexity : O(M), where M is the maximum number of nodes at any level in the binary tree.