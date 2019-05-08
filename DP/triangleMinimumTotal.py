'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
'''

def minimumTotal(triangle): # List[List[int]] -> int
  # bottom up solution
  ln = len(triangle)
  dp = triangle[ln-1] #

  # start from (n-2)th layer
  for row in range(ln-2, -1, -1):
    # compare each respective child
    for col in range(row+1):
      dp[col] = min(dp[col], dp[col+1]) + triangle[row][col]

  # return the value of the 0th (first) layer which is the min path
  return dp[0]

print(minimumTotal(triangle=[[2],
                            [3,4],
                           [6,5,7],
                          [4,1,8,3]]))
print(minimumTotal(triangle=[[-1],[2,3],[1,-1,-3]]))                                