'''
Given a positive integer n, find the least number of perfect square numbers (for example: 1, 4, 9, 16, ...) which sum to n.
'''
import math

def numSquares(n):
  # method 1
  # dp (Runtime error but works)
  # dp[n] indicates that the perfect squares count of the given n
  # MAX = float('inf')
  # dp = [0] + [MAX] * n

  # for i in range(1, n + 1):
  #   min_val = MAX
  #   j = 1
  #   while i - j*j >= 0:
  #     min_val = min(min_val, dp[i-j*j] + 1)
  #     j += 1

  #   dp[i] = min_val

  # return dp[-1]

  # method 2
  # bfs
  # The basic idea of this solution is a BSF search for shortest path, take 12 as an example, as shown below, the shortest path is 12-8-4-0:
  if n < 2:
    return n
  # store all 
  ps = [i**2 for i in range(1, math.ceil(math.sqrt(n)))]
  cnt = 0
  toCheck = {n}
  while toCheck:
    cnt += 1 # cur level
    temp = set() # or use a list
    for x in toCheck:
      # check each num in ps
      for y in ps:
        # found the target -> return number
        if x == y:
          return cnt
        # num in set > cur_num -> too big, so break
        if x < y:
          break
        # add the difference between target and ps to the set
        temp.add(x-y)
    toCheck = temp

  return cnt

print(numSquares(n=12))