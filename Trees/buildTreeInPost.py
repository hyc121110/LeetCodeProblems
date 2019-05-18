'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''

import ast

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  def buildTreeInPost(self, inorder, postorder):
    # slow version: O(n^2)
    # if not inorder or not postorder:
    #   return None
    # # set current root as the last element of the postorder list and pop it -> visited
    # root = TreeNode(postorder.pop())
    # # get index for splitting the inorder array
    # inorder_idx = inorder.index(root.val)

    # # set right and left recursively (order must be right -> left because postorder pops from right -> left)
    # root.right = self.buildTree(inorder[inorder_idx+1:], postorder)
    # root.left = self.buildTree(inorder[:inorder_idx], postorder)

    # return root

    # fast version: O(n) time and space (idea from above)
    # using dict to store idx
    map_inorder = {}
    # set val as key and idx as val for lookup
    for i, val in enumerate(inorder): map_inorder[val] = i

    def recur(low, high):
      if low > high:
        return None
      root = TreeNode(postorder.pop())
      mid = map_inorder[root.val]
      root.right = recur(mid+1, high)
      root.left = recur(low, mid-1)
      return root

    return recur(0, len(inorder)-1)


def stringToIntegerList(lst):
  lst = ast.literal_eval(lst)
  return list(map(int, lst))

def treeNodeToString(root):
  if not root:
    return "[]"
  output = ""
  queue = [root]
  current = 0
  while current != len(queue):
    node = queue[current]
    current = current + 1

    if not node:
      output += "null, "
      continue

    output += str(node.val) + ", "
    queue.append(node.left)
    queue.append(node.right)
  return "[" + output[:-2] + "]"

def main():
  import sys
  import io
  def readlines():
    for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
      yield line.strip('\n')

  lines = readlines()
  while True:
    try:
      line = next(lines)
      preorder = stringToIntegerList(line);
      line = next(lines)
      inorder = stringToIntegerList(line);
      
      ret = Solution().buildTreeInPost(preorder, inorder)

      out = treeNodeToString(ret);
      print(out)
    except StopIteration:
      break

if __name__ == '__main__':
    main()