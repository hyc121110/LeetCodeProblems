def maxDepth(root):
  # 1 line (slow)
  return 1 + max(maxDepth(root.left), maxDepth(root.right)) if root else 0

  # dfs (fast)
  # def helper(root, h):
  #   if not root: return 0
  #   left = helper(root.left, h+1)
  #   right = helper(root.right, h+1)
  #   if not left and not right: return h
  #   return max(left, right)
    
  # depth = 1
  # return helper(root, depth)

  # iterative (fastest)
  if not root:
    return 0

  tstack,h = [root],0
  
  #count number of levels
  while tstack:
    nextlevel = []
    while tstack:
      top = tstack.pop()
      if top.left:
        nextlevel.append(top.left)
      if top.right:
        nextlevel.append(top.right)
    tstack = nextlevel
    h+=1
  return h