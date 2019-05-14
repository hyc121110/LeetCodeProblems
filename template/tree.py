import ast

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  def function(tree):
    pass

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
      tree = stringToIntegerList(line);
      # line = next(lines)
      # inorder = stringToIntegerList(line);
      
      ret = Solution().function(tree)

      out = treeNodeToString(ret);
      print(out)
    except StopIteration:
      break

if __name__ == '__main__':