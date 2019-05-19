'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

def rob1(nums):
  # relation: rob(i) = max(rob(i-2) + cur_val, rob(i-1))

  # method 1: recursive (top-down) (slow)
  # def helper(nums, i):
  #   if i < 0:
  #     return 0
  #   return max(helper(nums, i-2) + nums[i], helper(nums, i-1))

  # if len(nums) == 1:
  #   return nums[0]
  # return helper(nums, len(nums)-1)

  # method 2: recursive memoization (top-down) (fastest)
  def helper(nums, i, dp):
    if i < 0: return 0
    if dp[i] >= 0: return dp[i]
    result = max(helper(nums, i-2, dp) + nums[i], helper(nums, i-1, dp))
    dp[i] = result
    return result

  dp = [-1] * (len(nums)+1)
  return helper(nums, len(nums)-1, dp)

  # # method 3: iterative, 2 variables (bottom-up)
  # if len(nums) == 0: return 0
  # prev1 = prev2 = 0
  # for num in nums:
  #   tmp = prev1
  #   prev1 = max(prev2 + num, prev1)
  #   prev2 = tmp
  # return prev1

print(rob1(nums=[1,2,3,4,5]))