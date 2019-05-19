'''
Given an unsorted array of integers, find the length of longest increasing subsequence.
'''

# using binary search to find the number needs update
# if x is larger than all tails, append it, increase the size by 1
# if tails[i-1] < x <= tails[i], update tails[i] because it is in between
def lengthOfLIS(nums):
  tails = [0] * len(nums)
  size = 0
  for x in nums:
    i, j = 0, size
    while i != j:
      m = (i + j) // 2
      if tails[m] < x:
        i = m + 1
      else:
        j = m
    tails[i] = x
    size = max(i + 1, size)
  return size

print(lengthOfLIS(nums=[10,9,2,5,3,7,101,18]))