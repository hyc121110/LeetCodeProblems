import ast

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  def buildTree(self, preorder, inorder):
    def build(stop):
      # make sure inorder is not empty and stop traversing when found 
      if inorder and inorder[-1] != stop:
        # set current root as the last element of the preorder list
        root = TreeNode(preorder.pop())
        # set the root's left children until its val is equal to inorder[-1]
        root.left = build(root.val)
        # all left child are set, pop inorder list
        inorder.pop()
        # set the root's right children until stop (splitting point of left and right)
        root.right = build(stop)
        return root

    # reverse both list for quicker pop
    preorder.reverse()
    inorder.reverse()
    return build(None)

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
      
      ret = Solution().buildTree(preorder, inorder)

      out = treeNodeToString(ret);
      print(out)
    except StopIteration:
      break

if __name__ == '__main__':
    main()