'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# for iterative solution
class Node:
    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
  # recursion
  # # base case
  # if not nums:
  #   return None
  # # find middle idx of nums
  # mid = len(nums) // 2
  
  # # set root as nums[mid]
  # root = TreeNode(nums[mid])
  
  # # divide array into two and set root.left as left array,
  # # root.right as right array
  # root.left = sortedArrayToBST(nums[:mid])
  # root.right = sortedArrayToBST(nums[mid+1:])
  
  # return root

  # iterative
  if not nums:
    return None
  # create dummy node
  root = TreeNode(0)
  stack = []
  node = Node(root, 0, len(nums)-1)

  # initial stack with dummy node
  stack.append(node)

  while stack:
    cur_node = stack.pop()
    mid = cur_node.left + (cur_node.right - cur_node.left) // 2
    cur_node.node.val = nums[mid]
    if cur_node.left < mid:
      cur_node.node.left = TreeNode(0)
      stack.append(Node(cur_node.node.left, cur_node.left, mid-1))
    if cur_node.right > mid:
      cur_node.node.right = TreeNode(0)
      stack.append(Node(cur_node.node.right, mid+1, cur_node.right))

  return root

print(sortedArrayToBST(nums=[-10,-3,0,5,9]))